"""C01/D01: explicit paired data, preserved order. See SOURCE_MAP and BSD notice."""
from __future__ import annotations
import numpy as np
from _common import parser, csv_data, paired, labels, title, figure, export

def validate_scale(values: np.ndarray, scale: str) -> None:
    if scale == "log" and np.any(values <= 0):
        raise ValueError("log scale requires strictly positive data")
    if scale == "logit" and np.any((values <= 0) | (values >= 1)):
        raise ValueError("logit scale requires data strictly between 0 and 1")

def main(argv: list[str] | None = None) -> None:
    p = parser(__doc__)
    p.add_argument("--kind", choices=["line", "scatter"], default="line")
    p.add_argument("--xscale", choices=["linear", "log", "symlog", "logit"], default="linear")
    p.add_argument("--yscale", choices=["linear", "log", "symlog", "logit"], default="linear")
    p.add_argument("--linthresh", type=float)
    args = p.parse_args(argv)
    if "symlog" in [args.xscale, args.yscale] and (
        args.linthresh is None or not np.isfinite(args.linthresh) or args.linthresh <= 0):
        p.error("symlog requires a finite positive --linthresh in data units")
    if args.demo:
        x = np.linspace(0, 8, 161)
        y = np.exp(-x/3)*np.cos(2*x)
    else:
        x, y = csv_data(args)
    x, y = paired(x, y)
    validate_scale(x, args.xscale); validate_scale(y, args.yscale)
    xlabel, ylabel = labels(args, "Time (s)", "Signal (a.u.)")
    import matplotlib
    matplotlib.use("Agg")
    with figure(args) as fig:
        ax = fig.add_subplot()
        if args.kind == "line":
            ax.plot(x, y, label="Signal")
        else:
            ax.scatter(x, y, s=12, alpha=0.7, label="Samples")
        for dim, scale in [("x", args.xscale), ("y", args.yscale)]:
            getattr(ax, f"set_{dim}scale")(scale, **({"linthresh": args.linthresh} if scale=="symlog" else {}))
        ax.set(xlabel=xlabel, ylabel=ylabel, title=title(args, "Damped signal" if args.demo else "Signal"))
        ax.legend()
        export(fig, args, "line_scatter", ["C01","D01","T01","S01"], {"samples":len(x), "order":"input order preserved"})

if __name__ == "__main__":
    main()
