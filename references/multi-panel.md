# 多面板网格与对齐

面板内部标签参见 layout-annotations.md；所有面板风格共性参见 colors-styling.md。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## M01 · GridSpec表达跨格和相对大小

**描述与目的**：用明确网格组织主要结果与辅助面板。

**适用条件**：面板尺寸不同或需要跨行跨列。

**输入要求**：布局规格；各面板数据可有不同形状。

**推荐实现**：创建GridSpec，用切片指定跨格区域；提前检查区域是否重叠。

**关键参数**：nrows/ncols、width_ratios、height_ratios、wspace/hspace；选择一种主要布局管理方式。

**常见错误**：把网格索引当数据坐标；跨格覆盖已有轴；同时强制所有轴尺寸/范围/比例一致。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(6, 4), constrained_layout=True)
grid = GridSpec(3, 3, figure=fig)
main = fig.add_subplot(grid[1:, 1:])
side = fig.add_subplot(grid[1:, 0])
top = fig.add_subplot(grid[0, 1:])
```

**证据与改编边界**：保留跨格机制，减少为三轴骨架；未复制原随机内容。源码文档 add_mosaic 片段不作为已验证API传播。

**原始出处**：

- [code/layout/layout-gridspec.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/layout-gridspec.py#L26-L48)，L26–L48。
- [rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L161-L200)，L161–L200。

## M02 · 散点与边际直方图对齐

**描述与目的**：主散点图与上下/左右分布应使用一致的坐标范围。

**适用条件**：同时看二维关系和两个单变量分布。

**输入要求**：同一批X,Y:(N,)；两组bin edges及明确范围。

**推荐实现**：2×2网格，上方x直方图、右侧横向y直方图；建议共享对应轴，隐藏重复标签。

**关键参数**：height_ratios=[1,5]、width_ratios=[5,1]；orientation="horizontal"。

**常见错误**：源例固定0–1范围会排除部分正态样本；21边界是20箱；以为原例已自动共享轴。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 5))
g = fig.add_gridspec(2, 2, height_ratios=[1, 5], width_ratios=[5, 1])
main = fig.add_subplot(g[1, 0])
top = fig.add_subplot(g[0, 0], sharex=main)
right = fig.add_subplot(g[1, 1], sharey=main)
# main.scatter(X,Y); top.hist(X,bins=x_edges)
# right.hist(Y,bins=y_edges,orientation="horizontal")
```

**证据与改编边界**：源例手工设范围；本骨架新增sharex/sharey，bins与数据由调用方提供，不照搬0–1范围。

**原始出处**：

- [code/layout/standard-layout-2.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/standard-layout-2.py#L19-L60)，L19–L60。
