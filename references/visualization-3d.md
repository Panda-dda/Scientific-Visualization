# 三维投影、网格与适配边界

本模块主要来自把三维几何投影到二维 Axes 的教材实现，不把它冒充通用三维物理引擎。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## G01 · MVP与齐次除法

**描述与目的**：把模型坐标依次变换至观察和投影空间。

**适用条件**：静态网格插图、需要可控正交/透视效果时。

**输入要求**：V:(N,3)；F:(M,3)零基三角面索引；MVP:(4,4)。

**推荐实现**：MVP=projection@view@model；扩充齐次坐标后乘矩阵并除w；显示坐标与原始物理坐标分别保存。

**关键参数**：旋转顺序、相机距离、fovy、aspect、near/far；w接近0需检查裁剪。

**常见错误**：漏掉齐次除法；把归一化几何当原始长度；用简单OBJ读取器读取任意v/vt/vn面记录。

**依赖**：NumPy；显示面片另需Matplotlib

**代码配方（适配版）**：

```python
import numpy as np

def project_vertices(vertices, mvp):
    h = np.c_[vertices, np.ones(len(vertices))] @ mvp.T
    if np.any(np.abs(h[:, 3]) < 1e-12):
        raise ValueError("Projection crosses w=0; clip geometry first")
    return h[:, :3] / h[:, 3, None]
```

**证据与改编边界**：重写投影步骤并增加零分母检查；此检查不实现近远裁剪。原OBJ读取器只适用于教材的简化输入。

**原始出处**：

- [code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L61-L96)，L61–L96。
- [rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L33-L40)，L33–L40。
- [rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L186-L198)，L186–L198。

## G02 · 按面深度排序并同步属性

**描述与目的**：使用画家算法控制小三角面的绘制顺序。

**适用条件**：相对小、不相交的三角形；静态展示优先。

**输入要求**：投影后T:(M,3,3)；逐面rgba:(M,4)。

**推荐实现**：按教材的投影约定取负平均z并排序；面颜色用相同索引重排。

**关键参数**：排序方向与相机约定一致；linewidth；背面剔除须知道顶点绕序。

**常见错误**：交叉面仍可能遮挡错误；各collection各自排序不能保证全局正确；深度色被误解为物理量。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
import numpy as np
from matplotlib.collections import PolyCollection

def draw_projected_faces(ax, triangles, rgba):
    order = np.argsort(-triangles[..., 2].mean(axis=1))
    faces = PolyCollection(triangles[order, :, :2],
                           facecolors=rgba[order], linewidth=0.25)
    ax.add_collection(faces)
    return faces
```

**证据与改编边界**：仅保留排序/绘制核心。不是深度缓冲实现，不保证交叉透明面正确。

**原始出处**：

- [rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L296-L305)，L296–L305。
- [code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L98-L117)，L98–L117。

## G03 · 高度场和轨迹共享变换，不共享输入语义

**描述与目的**：源 surf 是规则高度网格；轨迹需要时间顺序和真实空间单位。

**适用条件**：提取三维变换用于曲面或未来编队轨迹适配时。

**输入要求**：源surf要求方形Y:(n,n)，高度轴为Y、底面为XZ；轨迹建议P:(N,3)，保持时间顺序。

**推荐实现**：源surf每网格单元拆两三角形；轨迹适配可变换相邻点后形成线段，初末状态单独标注。

**关键参数**：camera角度在源函数中裁到0–90度；zoom>=0.1；轨迹单位、时间和视角需记录。

**常见错误**：把方形高度接口当通用非规则曲面；静默交换z与y；认为中点排序能解决所有轨迹遮挡。

**依赖**：NumPy；源glm/plot为本地模块，不能当PyPI依赖

**代码配方（适配版）**：

```python
import numpy as np

def trajectory_segments(projected_points):
    return np.stack((projected_points[:-1], projected_points[1:]), axis=1)
# 先调用 G01 的 project_vertices；按真实时间保留点顺序。
# 初末标记、裁剪和全局遮挡处理仍需应用层实现。
```

**证据与改编边界**：轨迹接口是从投影原语推导的适配建议，源库没有已验证的编队轨迹工作流。不能据此声称支持控制算法或稳定性分析。

**原始出处**：

- [code/unsorted/3d/plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/plot.py#L292-L372)，L292–L372。
- [code/unsorted/3d/glm.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/glm.py#L107-L138)，L107–L138。
