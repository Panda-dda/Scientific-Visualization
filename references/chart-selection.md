# 图型选择与适用边界

按问题和数据结构检索；选择准则是从源示例归纳，不是教材提供的完整决策算法。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## C01 · 折线、散点与直方图

**描述与目的**：区分有序变化、配对关系与单变量分布。

**适用条件**：时间/参数扫描用折线；独立样本的二维关系用散点；单变量分布用直方图。

**输入要求**：折线与散点 x,y:(N,)；直方图 samples:(N,)，edges:(B+1,) 严格递增。

**推荐实现**：选择图型后明确坐标单位；直方图检查边界外样本；折线仅在连接顺序有含义时使用。

**关键参数**：scatter 的 s/alpha；hist 的 bins/density；源码示例为计数。

**常见错误**：把无序样本连线；截掉范围外样本而未说明；把计数直方图称为概率密度。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
def draw_basic(ax, kind, x, y=None, bins=20):
    if kind == "line":
        return ax.plot(x, y)
    if kind == "scatter":
        return ax.scatter(x, y, s=15, alpha=0.25)
    if kind == "histogram":
        return ax.hist(x, bins=bins)
    raise ValueError(kind)
```

**证据与改编边界**：合并三个示例的 API，选择逻辑为归纳；调用方负责数据形状和单位检查，不从图推断因果关系。

**原始出处**：

- [code/ornaments/legend-alternatives.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/legend-alternatives.py#L23-L33)，L23–L33。
- [code/layout/standard-layout-2.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/standard-layout-2.py#L19-L60)，L19–L60。

## C02 · 数量、类别和偏差使用不同颜色编码

**描述与目的**：根据语义选择 sequential、qualitative、diverging 或 cyclic。

**适用条件**：连续量、无序组别、相对参考值偏差、周期角度等。

**输入要求**：数据语义；定量范围 vmin<vmax；发散色标 vmin<center<vmax。

**推荐实现**：先判断编码类型，再选择色图与 Normalize；有中心值的偏差用 TwoSlopeNorm。

**关键参数**：vmin、vmax、vcenter；类别顺序与颜色映射应显式保存。

**常见错误**：只换成发散色图却未设置中心；连续渐变暗示类别具有顺序；周期首尾不衔接。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from matplotlib.colors import TwoSlopeNorm

norm = TwoSlopeNorm(vmin=-3, vcenter=0, vmax=10)
# 示意参数来自教材；实际边界应来自任务定义。
```

**证据与改编边界**：保留教材中心化方法，统一正确导入；原文片段混用 colors/mpl 且有 Print 拼写，已规整。无新增统计含义。

**原始出处**：

- [rst/rules.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/rules.rst#L220-L229)，L220–L229。
- [rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L172-L217)，L172–L217。
