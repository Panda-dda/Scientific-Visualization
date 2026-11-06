# 物理尺寸、格式与混合渲染

教材数值是示例；目标期刊/版面要求由具体任务提供。字体嵌入验收与印刷色彩流程是尚未补足的知识。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## E01 · 按最终物理尺寸导出

**描述与目的**：figsize控制英寸尺寸，导出dpi控制栅格分辨率。

**适用条件**：论文单栏/双栏或明确插入尺寸的图。

**输入要求**：width_mm,height_mm>0；已完成Figure；格式及栅格dpi。

**推荐实现**：毫米除25.4换英寸；先确定最终尺寸再调字号。PDF/SVG保留可矢量化对象，内嵌图像仍有像素限制。

**关键参数**：figsize、savefig dpi、bbox_inches、facecolor；精确画布尺寸不要默认tight裁切。

**常见错误**：以为高DPI能修复源图模糊或字号太小；将600dpi当全部期刊标准；tight后仍声明固定像素尺寸。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from pathlib import Path

def export_figure(fig, output_dir, stem, width_mm, height_mm, dpi=300):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.set_size_inches(width_mm/25.4, height_mm/25.4)
    for ext in ("pdf", "svg", "png"):
        fig.savefig(output_dir / f"{stem}.{ext}", dpi=dpi, facecolor="white")
```

**证据与改编边界**：单位换算与三格式循环为提炼实现；参数300dpi是示意默认，不是投稿规格。调用方应给新输出名，避免覆盖已有结果。

**原始出处**：

- [rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L184-L218)，L184–L218。
- [rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L293-L369)，L293–L369。

## E02 · 只栅格化密集数据层

**描述与目的**：对数据Artist栅格化，保留文字、坐标和其他图层为矢量。

**适用条件**：大量点/线让PDF或SVG过大、打开缓慢。

**输入要求**：x,y:(N,)或复杂collection；最终物理尺寸和栅格dpi。

**推荐实现**：在数据Artist上设置rasterized=True；按实际输出大小检查栅格层质量。

**关键参数**：rasterized、dpi、marker size；对比导出体积和视觉结果，不能保证固定压缩比。

**常见错误**：把混合PDF称为纯矢量；把整图先转PNG；将低分辨率数据层无限放大用于海报。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
def dense_scatter(ax, x, y):
    return ax.scatter(x, y, s=2, rasterized=True)
# 在 E01 中选定导出dpi；标题与轴标签保持独立Artist。
```

**证据与改编边界**：保留教材rasterized方法，省略作者特定文件大小基准；没有进行本机导出测量。

**原始出处**：

- [rst/optimization.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/optimization.rst#L177-L221)，L177–L221。

## 用户选择 TEX / PGF

使用 `--formats tex` 生成独立 TEX 包装文件、PGF 绘图及必需的栅格 PNG；`--formats pgf` 不生成包装文件。需要 XeLaTeX 与 TikZ/PGF，包装文件编译需要 standalone 包。保持配套文件在同一目录，在该目录使用 XeLaTeX 编译。默认使用 LaTeX 字体；含中文时需另行配置和验证字体。缺依赖或生成失败应报告，不静默改成其他格式。PGF 是绘图命令，不等于 PGFPlots 数据源。

新增实现依据：[Matplotlib PGF 官方文档](https://matplotlib.org/stable/users/explain/text/pgf.html)。
