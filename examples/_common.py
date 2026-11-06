"""Shared CLI/export plumbing. Source mechanisms: P03/E01, SOURCE_MAP.md.
Adapted from Nicolas P. Rougier; see ../LICENSES/BSD-2-Clause.txt.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import platform
import shutil
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator
import numpy as np
import matplotlib as mpl
from matplotlib.figure import Figure

STYLE = Path(__file__).resolve().parents[1] / "assets/styles/scientific.mplstyle"

def positive(value: str) -> float:
    number = float(value)
    if not np.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("require a finite positive number")
    return number

def parser(description: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=description)
    source = p.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    p.add_argument("--synthetic-input", action="store_true", help="mark an external synthetic test dataset")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--formats", nargs="+", type=str.lower, choices=["pdf", "svg", "png", "pgf", "tex"], default=["pdf", "svg", "png"])
    p.add_argument("--width-mm", type=positive, default=120)
    p.add_argument("--height-mm", type=positive, default=85)
    p.add_argument("--dpi", type=positive, default=180)
    p.add_argument("--font-size", type=positive, default=9)
    p.add_argument("--line-width", type=positive, default=1.4)
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--x-column")
    p.add_argument("--y-column")
    p.add_argument("--xlabel")
    p.add_argument("--ylabel")
    p.add_argument("--title")
    return p

def paired(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or x.shape != y.shape or not len(x):
        raise ValueError("require nonempty, equally sized one-dimensional x/y")
    if not (np.isfinite(x).all() and np.isfinite(y).all()):
        raise ValueError("x/y must contain only finite numbers")
    return x, y

def csv_data(args: argparse.Namespace) -> tuple[np.ndarray, np.ndarray]:
    if not args.x_column or not args.y_column:
        raise ValueError("CSV input requires --x-column and --y-column")
    rows = []
    with args.input.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("CSV requires unique column names")
        for column in [args.x_column, args.y_column]:
            if column not in reader.fieldnames:
                raise ValueError(f"missing CSV column: {column}")
        for rownum, row in enumerate(reader, 2):
            values = []
            for column in [args.x_column, args.y_column]:
                try:
                    value = float(row[column])
                    if not np.isfinite(value):
                        raise ValueError("not finite")
                except (ValueError, TypeError) as exc:
                    raise ValueError(f"invalid CSV value at row {rownum}, column {column}") from exc
                values.append(value)
            rows.append(values)
    if not rows:
        raise ValueError("CSV contains no samples")
    return paired(*np.asarray(rows).T)

def labels(args: argparse.Namespace, x: str, y: str) -> tuple[str, str]:
    if args.input and (not args.xlabel or not args.ylabel):
        raise ValueError("real CSV input requires --xlabel/--ylabel with quantity and units")
    return args.xlabel or x, args.ylabel or y

def title(args: argparse.Namespace, default: str) -> str:
    result = args.title or default
    return result + ("\nSynthetic demonstration" if args.demo or args.synthetic_input else "")

@contextmanager
def figure(args: argparse.Namespace) -> Iterator[Figure]:
    # CLI chooses Agg in main; importing this module does not switch backends.
    import matplotlib.pyplot as plt
    with plt.style.context(str(STYLE)), mpl.rc_context({
        "font.size": args.font_size, "axes.labelsize": args.font_size,
        "axes.titlesize": args.font_size + 1, "lines.linewidth": args.line_width
    }):
        fig = plt.figure(figsize=(args.width_mm/25.4, args.height_mm/25.4),
                         constrained_layout=True)
        try:
            yield fig
        finally:
            plt.close(fig)

def export(fig: Figure, args: argparse.Namespace, stem: str,
           refs: list[str], details: dict | None = None) -> dict:
    if Path(stem).name != stem or stem in ["", ".", ".."]:
        raise ValueError("stem must be a single filename")
    dest = args.output_dir.resolve()
    dest.mkdir(parents=True, exist_ok=True)
    formats = list(dict.fromkeys(args.formats))
    if "tex" in formats or "pgf" in formats:
        if not shutil.which("xelatex"):
            raise RuntimeError("TEX/PGF export requires XeLaTeX and TikZ/PGF on PATH")
        formats = ["pgf"] + [ext for ext in formats if ext != "pgf"]
    targets = [dest/f"{stem}.{ext}" for ext in formats]
    log = dest/"run.json"
    if not args.overwrite:
        for target in [*targets, log]:
            if target.exists():
                raise FileExistsError(f"output exists: {target}; choose another directory or --overwrite")
    if args.input and args.input.resolve() in [*targets, log]:
        raise ValueError("output would overwrite input")
    meta = {
        "example": stem, "synthetic": args.demo or args.synthetic_input, "seed": args.seed if args.demo else None,
        "input": str(args.input.resolve()) if args.input else "synthetic demonstration",
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest() if args.input else None,
        "parameters": {k: str(v) if isinstance(v, Path) else v for k,v in vars(args).items()},
        "references": refs, "environment": {"python": platform.python_version(),
        "numpy": np.__version__, "matplotlib": mpl.__version__, "backend": mpl.get_backend()},
        "successful_files": [], "failed_files": [], "status": "running",
        "visual_inspection": "not_performed", "details": details or {}
    }
    try:
        for target in targets:
            try:
                if target.suffix == ".pgf":
                    # A real filename is required for raster sidecars. Stage the
                    # entire bundle before checking every destination for conflicts.
                    with tempfile.TemporaryDirectory() as staging:
                        staged = Path(staging)/target.name
                        with mpl.rc_context({"pgf.texsystem": "xelatex", "pgf.rcfonts": False,
                                             "pgf.preamble": ""}):
                            fig.savefig(staged, format="pgf", dpi=args.dpi, facecolor="white")
                        bundle = sorted(Path(staging).iterdir())
                        for source in bundle:
                            output = dest/source.name
                            if args.input and output == args.input.resolve():
                                raise ValueError("output would overwrite input")
                            if output.exists() and not args.overwrite:
                                raise FileExistsError(f"output exists: {output}")
                        for source in bundle:
                            with (dest/source.name).open("wb" if args.overwrite else "xb") as stream:
                                stream.write(source.read_bytes())
                            meta["successful_files"].append(source.name)
                    continue
                if target.suffix == ".tex":
                    if f"{stem}.pgf" not in meta["successful_files"]:
                        raise RuntimeError("required PGF export failed")
                    document = ("\\documentclass{standalone}\n\\usepackage{pgf}\n"
                                "\\usepackage{fontspec}\n\\begin{document}\n"
                                f"\\input{{{stem}.pgf}}\n\\end{{document}}\n")
                    with target.open("w" if args.overwrite else "x", encoding="utf-8") as stream:
                        stream.write(document)
                    meta["successful_files"].append(target.name)
                    continue
                # Exclusive create prevents an unintentional overwrite after preflight.
                with target.open("wb" if args.overwrite else "xb") as stream:
                    fig.savefig(stream, format=target.suffix[1:], dpi=args.dpi, facecolor="white")
                meta["successful_files"].append(target.name)
            except Exception as exc:
                meta["failed_files"].append({"file": target.name, "error": str(exc)})
        meta["status"] = ("passed" if not meta["failed_files"] else
                          "partial" if meta["successful_files"] else "failed")
    finally:
        with log.open("w" if args.overwrite else "x", encoding="utf-8") as stream:
            json.dump(meta, stream, ensure_ascii=False, indent=2)
    if meta["failed_files"]:
        raise RuntimeError(f"export {meta['status']}; see {log}")
    return meta
