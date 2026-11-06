# 字体、数学符号与文字可读性

最终尺寸换算见 publication-export.md；布局和坐标定位见 layout-annotations.md。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## T01 · 正文与数学字体分别配置

**描述与目的**：正文 font.family 和 mathtext.fontset 是不同设置。

**适用条件**：论文中需协调正文、刻度和公式；默认先采用内置 MathText。

**输入要求**：可用字体家族、字号 pt、数学字体集；公式字符串。

**推荐实现**：明确是否启用外部 TeX，检查实际解析字体；对缺失字体报告替代结果。

**关键参数**：font.family、font.size、mathtext.fontset、text.usetex；内置集如 stix/dejavusans。

**常见错误**：只改正文家族就认为公式也同步；默认认为所指定字体已安装；复制旧私有 _rebuild 调用。

**依赖**：Matplotlib；启用 TeX 时另需已安装 TeX 工具链

**代码配方（适配版）**：

```python
import matplotlib as mpl
from matplotlib.font_manager import FontProperties, findfont

settings = {"font.family": "DejaVu Sans", "font.size": 9,
            "mathtext.fontset": "dejavusans", "text.usetex": False}
resolved_font = findfont(FontProperties(family=settings["font.family"]))
# 用 mpl.rc_context(settings) 包住创建图与导出过程。
```

**证据与改编边界**：参数化原字体配置，并新增作用域与字体诊断建议；9 pt 是示意值，不是期刊标准。中文字体回退未获源库系统支持。

**原始出处**：

- [rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L42-L86)，L42–L86。
- [rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L100-L156)，L100–L156。
- [code/typography/typography-math-stacks.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/typography/typography-math-stacks.py#L10-L47)，L10–L47。

## T02 · 背景复杂时使用细描边

**描述与目的**：给必要文字增加反差边缘，减少大块底框遮挡。

**适用条件**：热图或图像上的短标注。

**输入要求**：已创建的 Text 对象；文字颜色、描边颜色和宽度。

**推荐实现**：使用 Stroke 后接 Normal；先选位置，再调整描边。

**关键参数**：linewidth 单位为 point；1.5 是教材示例起点，需按最终尺寸检查。

**常见错误**：描边过粗吞没字形；把所有文字都加底框；文字仍压住关键数据。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from matplotlib.patheffects import Stroke, Normal

def outline_text(text, width=1.5, color="white"):
    text.set_path_effects([Stroke(linewidth=width, foreground=color), Normal()])
    return text
```

**证据与改编边界**：将两组文字描边示例封装成接收 Text 的小函数。

**原始出处**：

- [rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L183-L192)，L183–L192。
- [code/typography/typography-legibility.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/typography/typography-legibility.py#L62-L70)，L62–L70。
