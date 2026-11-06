# 配色、图层与样式复用

颜色语义与中心化见 chart-selection.md；区间带含义见 principles.md。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## S01 · 公共样式与图专属参数分离

**描述与目的**：样式表保存共性；刻度、范围、标注保留在具体图中。

**适用条件**：多个结果图需要一致字体、线宽和边框。

**输入要求**：样式路径；各图的 ticks、limits、单位和标签。

**推荐实现**：参考 mystyle.txt 建立小型样式集；在受控作用域中创建、保存图；按数据设置轴。

**关键参数**：axes.spines、font、lines.linewidth；不要把所有图的 xlim/ylim 固定到样式中。

**常见错误**：机械复用正余弦示例的 π 刻度；样式相对路径依赖启动目录；误把一个模板当期刊通则。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from contextlib import contextmanager
from pathlib import Path
import matplotlib.pyplot as plt

@contextmanager
def styled_axes(style_path):
    with plt.style.context(str(Path(style_path))):
        fig, ax = plt.subplots()
        try:
            yield fig, ax  # 调用方在 with 内绘图和保存
        finally:
            plt.close(fig)
```

**证据与改编边界**：通过上下文管理器将创建、绘图和保存保留在同一作用域，退出时关闭图。源例采用全局 style.use。

**原始出处**：

- [rst/defaults.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/defaults.rst#L151-L237)，L151–L237。
- [code/defaults/defaults-step-5.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-5.py#L11-L30)，L11–L30。

## S02 · 渐变插值需注明颜色空间

**描述与目的**：自定义渐变时，编码后的 sRGB 直接插值与线性 RGB/Lab 插值不同。

**适用条件**：已有明确端点颜色，需要比较渐变而非选择现成色图时。

**输入要求**：c0,c1:RGB 三元组，范围0–1；n>=2。

**推荐实现**：按选定空间转换后插值，再转回 sRGB；检查输出范围与视觉连续性。

**关键参数**：space、n；源码 mode="RGB" 指线性 RGB，不等同 sRGB。

**常见错误**：把通道均值当感知均匀；误认为 Lab 插值一定适用于任何科学编码；额外维度未清理。

**依赖**：NumPy、scikit-image；显示渐变时另需 Matplotlib

**代码配方（适配版）**：

```python
import numpy as np
from skimage.color import rgb2lab, lab2rgb

def lab_gradient(c0, c1, n=256):
    endpoints = np.asarray([c0, c1], dtype=float).reshape(1, 2, 3)
    lab = rgb2lab(endpoints)[0]
    t = np.linspace(0, 1, n)[:, None]
    mix = (1-t)*lab[0] + t*lab[1]
    return lab2rgb(mix.reshape(1, n, 3))[0]
```

**证据与改编边界**：重写为固定返回 (n,3) 的 Lab 分支，避免原转换辅助函数的额外轴歧义；未运行验证。

**原始出处**：

- [rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L35-L55)，L35–L55。
- [code/colors/color-gradients.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/color-gradients.py#L10-L63)，L10–L63。
