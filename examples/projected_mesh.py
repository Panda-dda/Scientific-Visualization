"""G01/G02: orthographic mesh projection. Rougier mechanisms; see BSD notice."""
from __future__ import annotations
import numpy as np
from _common import parser, title, figure, export

def validate_mesh(vertices: np.ndarray, faces: np.ndarray) -> None:
    if vertices.ndim!=2 or vertices.shape[1]!=3 or not len(vertices) or not np.isfinite(vertices).all():
        raise ValueError("vertices must be finite nonempty (N,3)")
    if faces.ndim!=2 or faces.shape[1]!=3 or not len(faces) or not np.issubdtype(faces.dtype,np.integer):
        raise ValueError("faces must be nonempty integer (M,3)")
    if np.any(faces<0) or np.any(faces>=len(vertices)):
        raise ValueError("face index outside vertex range")
    normals=np.cross(vertices[faces[:,1]]-vertices[faces[:,0]],
                     vertices[faces[:,2]]-vertices[faces[:,0]])
    if np.any(np.linalg.norm(normals,axis=1)<=1e-12):
        raise ValueError("degenerate triangles")

def project(vertices: np.ndarray, mvp: np.ndarray) -> np.ndarray:
    h=np.c_[vertices,np.ones(len(vertices))]@mvp.T
    if np.any(np.abs(h[:,3])<1e-12) or not np.isfinite(h).all():
        raise ValueError("invalid homogeneous projection")
    return h[:,:3]/h[:,3,None]

def main(argv: list[str] | None = None) -> None:
    p=parser(__doc__)
    p.add_argument("--azimuth",type=float,default=35)
    p.add_argument("--elevation",type=float,default=25)
    p.add_argument("--unit",default="input units")
    args=p.parse_args(argv)
    if not np.isfinite([args.azimuth,args.elevation]).all():
        p.error("camera angles must be finite")
    if args.demo:
        vertices=np.array([[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
                           [-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],float)
        faces=np.array([[0,1,2],[0,2,3],[4,6,5],[4,7,6],[0,4,5],[0,5,1],
                        [1,5,6],[1,6,2],[2,6,7],[2,7,3],[3,7,4],[3,4,0]])
    else:
        with np.load(args.input,allow_pickle=False) as data:
            vertices=np.asarray(data["vertices"],dtype=float)
            faces=data["faces"]
    validate_mesh(vertices,faces)
    az,el=np.deg2rad([args.azimuth,args.elevation])
    rz=np.array([[np.cos(az),-np.sin(az),0],[np.sin(az),np.cos(az),0],[0,0,1]])
    rx=np.array([[1,0,0],[0,np.cos(el),-np.sin(el)],[0,np.sin(el),np.cos(el)]])
    matrix=np.eye(4); matrix[:3,:3]=rx@rz
    projected=project(vertices,matrix)
    triangles=projected[faces]
    # Camera looks along +z: larger z is farther and must be drawn first.
    order=np.argsort(-triangles[:,:,2].mean(axis=1),kind="stable")
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib.collections import PolyCollection
    colors=matplotlib.colormaps["Blues"](np.linspace(.35,.85,len(faces)))
    with figure(args) as fig:
        ax=fig.add_subplot()
        ax.add_collection(PolyCollection(triangles[order,:,:2],facecolors=colors[order],
                                        edgecolors="white",linewidths=.4))
        ax.autoscale_view(); ax.margins(.12)
        ax.set_aspect("equal",adjustable="box")
        unit="a.u." if args.demo else args.unit
        ax.set(xlabel=f"Projected u ({unit})",ylabel=f"Projected v ({unit})",
               title=title(args,"Orthographic mesh"))
        export(fig,args,"projected_mesh",["G01","G02"],
               {"vertices":len(vertices),"faces":len(faces),"face_order":order.tolist(),
                "matrix":matrix.tolist(),"colors":"face identity only",
                "limitations":"no clipping; painter sorting cannot resolve intersecting or transparent faces"})

if __name__ == "__main__":
    main()
