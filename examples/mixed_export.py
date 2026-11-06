"""E01/E02: rasterize only dense data, preserve text/axes. Rougier BSD sources."""
from __future__ import annotations
import numpy as np
from _common import parser, csv_data, labels, title, figure, export

def main(argv: list[str] | None = None) -> None:
    args=parser(__doc__).parse_args(argv)
    if args.demo:
        rng=np.random.default_rng(args.seed)
        x=rng.normal(size=20000)
        y=.5*x+rng.normal(scale=.8,size=len(x))
    else:
        x,y=csv_data(args)
    xlabel,ylabel=labels(args,"Variable x (a.u.)","Variable y (a.u.)")
    import matplotlib
    matplotlib.use("Agg")
    with figure(args) as fig:
        ax=fig.add_subplot()
        ax.scatter(x,y,s=2,alpha=.15,rasterized=True)
        ax.set(xlabel=xlabel,ylabel=ylabel,title=title(args,"Dense samples"))
        export(fig,args,"mixed_export",["E01","E02"],
               {"samples":len(x),"rasterized":"scatter only","encoding":"alpha overlap, not probability density"})

if __name__ == "__main__":
    main()
