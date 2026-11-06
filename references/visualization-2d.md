# 二维尺度、几何与集合对象

基本图型见 chart-selection.md；这里补足尺度定义域、几何比例和大量线段。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## D01 · 按定义域选择坐标尺度

**描述与目的**：log、symlog、logit 表达不同数值结构。

**适用条件**：倍数跨度、跨零宽范围、严格介于0与1的比例。

**输入要求**：x或y:(N,)；log要求正值；logit要求0<值<1；symlog线性阈值>0。

**推荐实现**：保持原始数值，选择轴尺度；阈值根据单位和研究问题指定。

**关键参数**：set_xscale/set_yscale；linthresh 为补充参数化建议。

**常见错误**：先手动取对数又设log轴；悄悄丢弃零或负值；把logit用于边界0/1。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
def set_signal_scale(ax, scale, linear_threshold=None):
    if scale == "symlog":
        if linear_threshold is None or linear_threshold <= 0:
            raise ValueError("Specify positive threshold in data units")
        ax.set_yscale(scale, linthresh=linear_threshold)
    else:
        ax.set_yscale(scale)
```

**证据与改编边界**：教材给出尺度语义；添加 linthresh 参数及输入检查，原数据定义域仍由调用方校验。

**原始出处**：

- [rst/projections.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/projections.rst#L24-L86)，L24–L86。
- [code/scales-projections/scales-comparison.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/scales-projections/scales-comparison.py#L46-L78)，L46–L78。

## D02 · 等比例轴保持二维几何

**描述与目的**：数据单位的长度一致性与画布是否正方形无关。

**适用条件**：同量纲空间坐标、几何轮廓或方向需要保持时。

**输入要求**：x/y数据及显示范围；单位可比较。

**推荐实现**：设置 equal aspect，再选择保留范围还是调整轴框；对不同量纲的一般统计关系不机械强制等比例。

**关键参数**：aspect、adjustable、xlim/ylim；固定比例、范围、轴框尺寸可能过度约束。

**常见错误**：把正方形 figsize 当等比例；把 equal 当正方形轴框；静默改范围以填满版面。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
def set_geometry_axes(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
```

**证据与改编边界**：由教材宽高比约束提炼接口；显式选择 adjustable="box" 是保留数据范围的适配决定。

**原始出处**：

- [rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L21-L44)，L21–L44。
- [rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L108-L109)，L108–L109。
- [code/layout/layout-aspect.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/layout-aspect.py#L28-L61)，L28–L61。

## D03 · 用集合对象绘制多线与分段色彩

**描述与目的**：LineCollection 可减少大量独立 Artist 的管理开销。

**适用条件**：多条轨迹、重复实验信号、需要逐段着色的二维路径。

**输入要求**：点列列表，每条(N_i,2)；逐段绘图时 segments:(N-1,2,2)；颜色与线段数量匹配。

**推荐实现**：相邻点组成线段并添加集合；显式设置轴范围；量值着色须传入真实量值和色标。

**关键参数**：linewidths、alpha、colors、norm；重复路径的透明叠加语义需另检查。

**常见错误**：把纹理色当速度；只测Artist创建耗时就声称完整导出加速；忘记范围设置。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
import numpy as np
from matplotlib.collections import LineCollection

def colored_segments(ax, points, values, cmap, norm):
    segments = np.stack((points[:-1], points[1:]), axis=1)
    lines = LineCollection(segments, cmap=cmap, norm=norm)
    lines.set_array(np.asarray(values))  # 每条线段一个值
    ax.add_collection(lines)
    return lines
```

**证据与改编边界**：从彩线/集合例提炼接口；源colored-plot按线段顺序取色，此处改为调用方提供逐段量值和norm。windmap 的颜色实际来自弧长取模加随机相位，不是其 speed 数组；该示例不能作为速度色标依据。

**原始出处**：

- [code/colors/colored-plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/colored-plot.py#L13-L33)，L13–L33。
- [rst/optimization.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/optimization.rst#L84-L117)，L84–L117。
- [code/showcases/windmap.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/showcases/windmap.py#L203-L231)，L203–L231。
