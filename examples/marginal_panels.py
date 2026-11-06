"""M01/M02: scatter with count marginals. Adapted from Rougier; BSD notice."""
from __future__ import annotations
import numpy as np
from _common import parser, csv_data, labels, title, figure, export

def main(argv: list[str] | None = None) -> None:
    p = parser(__doc__)
    p.add_argument("--bins", type=int, default=24)
    args = p.parse_args(argv)
    if args.bins < 1:
        p.error("--bins must be positive")
    if args.demo:
        rng = np.random.default_rng(args.seed)
        x = rng.normal(size=1200)
        y = .65*x + rng.normal(scale=.7, size=len(x))
    else:
        x,y = csv_data(args)
    xlabel,ylabel = labels(args, "Variable x (a.u.)", "Variable y (a.u.)")
    xe,ye = np.histogram_bin_edges(x,bins=args.bins),np.histogram_bin_edges(y,bins=args.bins)
    xc,yc = np.histogram(x,xe)[0],np.histogram(y,ye)[0]
    if xc.sum()!=len(x) or yc.sum()!=len(y):
        raise ValueError("histogram drops samples")
    import matplotlib
    matplotlib.use("Agg")
    with figure(args) as fig:
        g=fig.add_gridspec(2,2,height_ratios=[1,4],width_ratios=[4,1])
        main=fig.add_subplot(g[1,0])
        top=fig.add_subplot(g[0,0],sharex=main)
        side=fig.add_subplot(g[1,1],sharey=main)
        main.scatter(x,y,s=5,alpha=.25,rasterized=True)
        top.hist(x,bins=xe,color="C0")
        side.hist(y,bins=ye,orientation="horizontal",color="C0")
        main.set(xlabel=xlabel,ylabel=ylabel)
        top.set_ylabel("Count"); side.set_xlabel("Count")
        top.tick_params(labelbottom=False); side.tick_params(labelleft=False)
        fig.suptitle(title(args,"Joint distribution"))
        export(fig,args,"marginal_panels",["M01","M02"],
               {"samples":len(x),"x_counts":xc.tolist(),"y_counts":yc.tolist(),
                "x_edges":xe.tolist(),"y_edges":ye.tolist()})

if __name__ == "__main__":
    main()
