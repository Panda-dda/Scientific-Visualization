# 科学表达与可重复性

数据含义、视觉编码、证据边界；图型选择另见 chart-selection.md。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## P01 · 面积编码与轴基线

**描述与目的**：让几何面积而非半径对应数量，避免视觉夸大。

**适用条件**：用圆表示非负数量，或审查绝对量柱图。

**输入要求**：values:(N,) 非负；reference_value>0；reference_radius>0。

**推荐实现**：圆半径按数量比的平方根缩放；柱图需要可解释的基线。零基线建议针对柱长编码，不套用于所有折线图。

**关键参数**：reference_value、reference_radius；Circle 用半径，scatter 的 s 表示面积量。

**常见错误**：复制教学反例中的线性半径；把截断柱轴的差异解释为真实倍数；把强调效果解释为统计显著性。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
import numpy as np

def area_radii(values, reference_value, reference_radius):
    values = np.asarray(values, dtype=float)
    if reference_value <= 0 or reference_radius <= 0 or np.any(values < 0):
        raise ValueError("Require nonnegative values and positive references")
    return reference_radius * np.sqrt(values / reference_value)
```

**证据与改编边界**：代码等价改写原面积公式，增加输入检查；柱图基线归纳为建议。未做统计检验。

**原始出处**：

- [rst/rules.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/rules.rst#L243-L294)，L243–L294。
- [code/rules/rule-7.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/rules/rule-7.py#L12-L18)，L12–L18。

## P02 · 把显示效果与统计量分开

**描述与目的**：颜色叠加、渲染密度与流线纹理可能只是展示效果。

**适用条件**：带状区间、密集散点或多条曲线需要解释颜色时。

**输入要求**：x,mean,spread:(N,)；spread>=0，单位一致；区间含义由数据提供方确定。

**推荐实现**：显式传入已计算的上下界，用 fill_between 绘制；图注说明 SD、SE、CI 或其他含义及计算来源。

**关键参数**：alpha、zorder、颜色；图层顺序会改变重叠颜色。

**常见错误**：把渲染通道滤波称为 KDE；把 SD 带当置信区间；从颜色深浅直接读取样本概率。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
def draw_band(ax, x, mean, spread, meaning, color="C0"):
    ax.fill_between(x, mean-spread, mean+spread,
                    color=color, alpha=0.25, zorder=1)
    line, = ax.plot(x, mean, color=color, zorder=2, label=meaning)
    return line
```

**证据与改编边界**：由源带状图提炼接口；数组由调用方提供。统计量定义、样本量及区间计算属于补充要求，源库未给完整统计规范。

**原始出处**：

- [rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L151-L161)，L151–L161。
- [code/colors/alpha-vs-color.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/alpha-vs-color.py#L186-L213)，L186–L213。
- [code/colors/alpha-scatter.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/alpha-scatter.py#L25-L60)，L25–L60。

## P03 · 分离数据、样式和输出

**描述与目的**：教学脚本中的全局状态不应成为复用接口的隐式输入。

**适用条件**：复用同一图型绘制不同实验或批量导图。

**输入要求**：显式数据数组、style_path、output_path；随机数据需另给 seed。

**推荐实现**：在函数内接收 Axes；样式作用域内完成绘图和保存；源文件只读，输出路径指向独立目录。

**关键参数**：style_path 使用已解析路径；随机种子在造数阶段记录。

**常见错误**：导入模块即执行绘图；全局 rcParams 泄漏；以当前工作目录解析所有资源；误把合成示例当实验结果。

**依赖**：NumPy、Matplotlib

**代码配方（适配版）**：

```python
import matplotlib.pyplot as plt

def render_line(x, y, style_path, output_path):
    with plt.style.context(style_path):
        fig, ax = plt.subplots()
        ax.plot(x, y)
        fig.savefig(output_path)
        plt.close(fig)
```

**证据与改编边界**：源例使用 style.use；style.context、参数化路径与生命周期管理是新增工程封装，未声称源例已这样实现。

**原始出处**：

- [rst/defaults.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/defaults.rst#L151-L237)，L151–L237。
- [code/defaults/defaults-step-4.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-4.py#L11-L20)，L11–L20。
