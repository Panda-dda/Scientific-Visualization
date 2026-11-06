# 来源映射与改编记录

作者：Nicolas P. Rougier。书名：Scientific Visualization: Python + Matplotlib。原仓库：[howToDraw](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/README.md)。基线：`62fa569f30333c817c13e4dc757877c1192fd15a`。提炼与参数化改编：本项目，2026-11-06。

## 许可记录

依据 [LICENSE.txt](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/LICENSE.txt) 和 [序言](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/00-preface.rst#L93-L107) L93–L107：书稿 CC BY-NC-SA 4.0；图件默认 CC BY 4.0、代码默认 BSD 2-Clause，均以“另有声明”为例外。

提炼文档保留书稿署名与改编说明，按 CC BY-NC-SA 4.0 标识；代码片段仅是与各条来源关联的适配草案，不把混合来源统一重新许可。后续分发可执行代码应逐文件保留适用版权与条件。

明确例外：`code/anatomy/figure-dpi.py`、`inch-cm.py`、`pixel-font.py` 各自头部声明 CC BY-NC-SA 4.0，不能因扩展名为.py就写成BSD。此次未搬运这些完整文件。Roboto附Apache许可，Source字族附SIL OFL许可，未复制字体。

## 技术对应表

| ID / 知识文档 | 原始位置 | 改编说明 |
|---|---|---|
| P01 · [principles](references/principles.md) | [rst/rules.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/rules.rst#L243-L294) L243–L294；[code/rules/rule-7.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/rules/rule-7.py#L12-L18) L12–L18 | 代码等价改写原面积公式，增加输入检查；柱图基线归纳为建议。未做统计检验。 |
| P02 · [principles](references/principles.md) | [rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L151-L161) L151–L161；[code/colors/alpha-vs-color.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/alpha-vs-color.py#L186-L213) L186–L213；[code/colors/alpha-scatter.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/alpha-scatter.py#L25-L60) L25–L60 | 由源带状图提炼接口；数组由调用方提供。统计量定义、样本量及区间计算属于补充要求，源库未给完整统计规范。 |
| P03 · [principles](references/principles.md) | [rst/defaults.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/defaults.rst#L151-L237) L151–L237；[code/defaults/defaults-step-4.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-4.py#L11-L20) L11–L20 | 源例使用 style.use；style.context、参数化路径与生命周期管理是新增工程封装，未声称源例已这样实现。 |
| C01 · [chart-selection](references/chart-selection.md) | [code/ornaments/legend-alternatives.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/legend-alternatives.py#L23-L33) L23–L33；[code/layout/standard-layout-2.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/standard-layout-2.py#L19-L60) L19–L60 | 合并三个示例的 API，选择逻辑为归纳；调用方负责数据形状和单位检查，不从图推断因果关系。 |
| C02 · [chart-selection](references/chart-selection.md) | [rst/rules.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/rules.rst#L220-L229) L220–L229；[rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L172-L217) L172–L217 | 保留教材中心化方法，统一正确导入；原文片段混用 colors/mpl 且有 Print 拼写，已规整。无新增统计含义。 |
| T01 · [typography](references/typography.md) | [rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L42-L86) L42–L86；[rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L100-L156) L100–L156；[code/typography/typography-math-stacks.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/typography/typography-math-stacks.py#L10-L47) L10–L47 | 参数化原字体配置，并新增作用域与字体诊断建议；9 pt 是示意值，不是期刊标准。中文字体回退未获源库系统支持。 |
| T02 · [typography](references/typography.md) | [rst/typography.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/typography.rst#L183-L192) L183–L192；[code/typography/typography-legibility.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/typography/typography-legibility.py#L62-L70) L62–L70 | 将两组文字描边示例封装成接收 Text 的小函数。 |
| S01 · [colors-styling](references/colors-styling.md) | [rst/defaults.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/defaults.rst#L151-L237) L151–L237；[code/defaults/defaults-step-5.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-5.py#L11-L30) L11–L30 | 通过上下文管理器将创建、绘图和保存保留在同一作用域，退出时关闭图。源例采用全局 style.use。 |
| S02 · [colors-styling](references/colors-styling.md) | [rst/colors.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/colors.rst#L35-L55) L35–L55；[code/colors/color-gradients.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/color-gradients.py#L10-L63) L10–L63 | 重写为固定返回 (n,3) 的 Lab 分支，避免原转换辅助函数的额外轴歧义；未运行验证。 |
| L01 · [layout-annotations](references/layout-annotations.md) | [rst/coordinates.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/coordinates.rst#L19-L37) L19–L37；[rst/coordinates.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/coordinates.rst#L130-L171) L130–L171；[code/coordinates/transforms-letter.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/coordinates/transforms-letter.py#L24-L36) L24–L36 | 参数化原面板字母示例，明确偏移单位为 point。 |
| L02 · [layout-annotations](references/layout-annotations.md) | [rst/ornaments.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/ornaments.rst#L70-L83) L70–L83；[code/ornaments/legend-alternatives.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/legend-alternatives.py#L35-L106) L35–L106 | 把源码固定索引改为末端索引，并使用物理偏移；不能保证任意数据标签无重叠。 |
| L03 · [layout-annotations](references/layout-annotations.md) | [code/ornaments/annotation-zoom.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/annotation-zoom.py#L15-L79) L15–L79；[rst/ornaments.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/ornaments.rst#L195-L205) L195–L205 | 仅封装区域和连接；调用方须在两轴绘制同一数据。布局位置需与所选连接边一致。 |
| D01 · [visualization-2d](references/visualization-2d.md) | [rst/projections.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/projections.rst#L24-L86) L24–L86；[code/scales-projections/scales-comparison.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/scales-projections/scales-comparison.py#L46-L78) L46–L78 | 教材给出尺度语义；添加 linthresh 参数及输入检查，原数据定义域仍由调用方校验。 |
| D02 · [visualization-2d](references/visualization-2d.md) | [rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L21-L44) L21–L44；[rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L108-L109) L108–L109；[code/layout/layout-aspect.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/layout-aspect.py#L28-L61) L28–L61 | 由教材宽高比约束提炼接口；显式选择 adjustable="box" 是保留数据范围的适配决定。 |
| D03 · [visualization-2d](references/visualization-2d.md) | [code/colors/colored-plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/colored-plot.py#L13-L33) L13–L33；[rst/optimization.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/optimization.rst#L84-L117) L84–L117；[code/showcases/windmap.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/showcases/windmap.py#L203-L231) L203–L231 | 从彩线/集合例提炼接口；源colored-plot按线段顺序取色，此处改为调用方提供逐段量值和norm。windmap 的颜色实际来自弧长取模加随机相位，不是其 speed 数组；该示例不能作为速度色标依据。 |
| G01 · [visualization-3d](references/visualization-3d.md) | [code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L61-L96) L61–L96；[rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L33-L40) L33–L40；[rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L186-L198) L186–L198 | 重写投影步骤并增加零分母检查；此检查不实现近远裁剪。原OBJ读取器只适用于教材的简化输入。 |
| G02 · [visualization-3d](references/visualization-3d.md) | [rst/threed.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/threed.rst#L296-L305) L296–L305；[code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L98-L117) L98–L117 | 仅保留排序/绘制核心。不是深度缓冲实现，不保证交叉透明面正确。 |
| G03 · [visualization-3d](references/visualization-3d.md) | [code/unsorted/3d/plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/plot.py#L292-L372) L292–L372；[code/unsorted/3d/glm.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/glm.py#L107-L138) L107–L138 | 轨迹接口是从投影原语推导的适配建议，源库没有已验证的编队轨迹工作流。不能据此声称支持控制算法或稳定性分析。 |
| M01 · [multi-panel](references/multi-panel.md) | [code/layout/layout-gridspec.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/layout-gridspec.py#L26-L48) L26–L48；[rst/layout.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/layout.rst#L161-L200) L161–L200 | 保留跨格机制，减少为三轴骨架；未复制原随机内容。源码文档 add_mosaic 片段不作为已验证API传播。 |
| M02 · [multi-panel](references/multi-panel.md) | [code/layout/standard-layout-2.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/layout/standard-layout-2.py#L19-L60) L19–L60 | 源例手工设范围；本骨架新增sharex/sharey，bins与数据由调用方提供，不照搬0–1范围。 |
| E01 · [publication-export](references/publication-export.md) | [rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L184-L218) L184–L218；[rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L293-L369) L293–L369 | 单位换算与三格式循环为提炼实现；参数300dpi是示意默认，不是投稿规格。调用方应给新输出名，避免覆盖已有结果。 |
| E02 · [publication-export](references/publication-export.md) | [rst/optimization.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/optimization.rst#L177-L221) L177–L221 | 保留教材rasterized方法，省略作者特定文件大小基准；没有进行本机导出测量。 |
| B01 · [debugging](references/debugging.md) | [rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L158-L243) L158–L243；[code/defaults/defaults-step-4.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-4.py#L11-L20) L11–L20；[code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L80-L96) L80–L96 | 诊断顺序与隔离输出属于工程建议；本阶段未执行此诊断片段。 |
| B02 · [debugging](references/debugging.md) | [code/colors/color-wheel.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/color-wheel.py#L29-L41) L29–L41；[code/unsorted/3d/plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/plot.py#L245-L265) L245–L265 | 提出最小修正规则；未改原文件、未声明修复已通过。3D矩阵非对称投影另待数值验证。 |
| B03 · [animation](references/animation.md) | [rst/animation.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/animation.rst#L18-L91) L18–L91 | 由教材动画接口改写；:i+1是静态边界修正，未运行验证。动画是可选扩展，不是核心强制依赖。 |

## 引用源文件的显式声明摘录

以下从引用文件前12行自动记录声明线，便于后续包装核对；没有显式行时回查仓库默认说明。这不是对每个第三方素材的权属审计。

- `code/colors/alpha-scatter.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/colors/alpha-vs-color.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/colors/color-gradients.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/colors/color-wheel.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/colors/colored-plot.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/coordinates/transforms-letter.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: Creative Commons BY-NC-SA International 4.0
- `code/defaults/defaults-step-4.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/defaults/defaults-step-5.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/layout/layout-aspect.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/layout/layout-gridspec.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/layout/standard-layout-2.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/ornaments/annotation-zoom.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/ornaments/legend-alternatives.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/rules/rule-7.py`：前12行无 Author/License 字段；需结合仓库默认声明。
- `code/scales-projections/scales-comparison.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/showcases/windmap.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/threed/bunny.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: BSD
- `code/typography/typography-legibility.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: Creative Commons BY-NC-SA International 4.0
- `code/typography/typography-math-stacks.py`：L3: # Author:  Nicolas P. Rougier；L4: # License: Creative Commons BY-NC-SA International 4.0
- `code/unsorted/3d/glm.py`：前12行无 Author/License 字段；需结合仓库默认声明。
- `code/unsorted/3d/plot.py`：前12行无 Author/License 字段；需结合仓库默认声明。
- `rst/anatomy.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/animation.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/colors.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/coordinates.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/defaults.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/layout.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/optimization.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/ornaments.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/projections.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: BSD
- `rst/rules.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/threed.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0
- `rst/typography.rst`：L3: .. Author:  Nicolas P. Rougier；L4: .. License: Creative Commons BY-NC-SA International 4.0

## 发布文件与改编状态

文档与短配方是来源支持的提炼，不统一宣称逐段运行通过。核心例子的执行和视觉结果见 README。

| 发布实现 | 技术ID | 改编 |
|---|---|---|
| examples/_common.py | P03 E01 | 新增输入校验、文件预检、局部样式、版本/哈希记录和部分失败报告 |
| examples/line_scatter.py | C01 D01 T01 S01 | 新增CSV接口、尺度定义域检查、合成演示标记 |
| examples/marginal_panels.py | M01 M02 | 新增共享轴、直方图计数与边界记录 |
| examples/projected_mesh.py | G01 G02 | 正交旋转投影、NPZ输入检查、面排序和属性同步；不含裁剪或透明排序保证 |
| examples/mixed_export.py | E01 E02 | 密集数据层单独栅格化，固定物理画布 |
| assets/styles/scientific.mplstyle | S01 T01 | 可覆盖默认值；PDF TrueType与SVG文字设置为新增导出选择 |

## 引用文件SHA-256

- LICENSE.txt: fe46de7e04df7a3c29869354f53bc57102bca82f59c4b6735089cda8d54521c2
- README.md: 7afa7f29cbcf61320b5960cd5d8f99ad9c1b706c185fcb75359e737d32d24574
- code/colors/alpha-scatter.py: b98b8d7aa25284201a95836cceb2e6b2493315424dea8f9a89693595321d9bde
- code/colors/alpha-vs-color.py: 001ba5d306d7ca930252cb50849dd550faee2449946ae8387b9b15bf7998956e
- code/colors/color-gradients.py: e5820df975812a323e36197735a1616bf6bb62dacc7fdab503a19474fbfcc244
- code/colors/color-wheel.py: 33a700b7f92e87998d8a2b727f99cb6e975f608a17e870490832f534550af784
- code/colors/colored-plot.py: 686a46658de069311c8288c3505da80f4874448ea7064c51e9178f9e39bdbe6c
- code/coordinates/transforms-letter.py: 78a725647941d9699bf0332a8bbbb5c6054d1d97799fd12bb898a7f1ee07a8d6
- code/defaults/defaults-step-4.py: e578eab680b09da16467a8de7c0e47e8f7346a1f72d2c35bbffd7794e57d469c
- code/defaults/defaults-step-5.py: 76727bdd9dd39ad8757a6d4cda3a7af5b29c864fbff2819ae341675ccfdd509f
- code/layout/layout-aspect.py: 500cb9af5e0e26bca33c887ae0b8499c797dde898538ab1213a84ee6f2ffdd2e
- code/layout/layout-gridspec.py: 8b60b2164b3f9fe2d3b292f875ea9a109604d158b793fbe24fbd0c8b20f139b7
- code/layout/standard-layout-2.py: 1afe8b6a921c9dfb0e5de3ef5d46467628f49a501fea07b55f2ac5e10f8d27ab
- code/ornaments/annotation-zoom.py: bbd8d53f33e2b262a2bf890bde0a922276633cdc7e0c7a22feb0ad7662edb62a
- code/ornaments/legend-alternatives.py: 6267ffcaa841448bc8a292454c3ed9bd390d4734675290c8039f67557d9ad849
- code/rules/rule-7.py: bd7cef575e10aabbeacd30c6bb92cd379c315c4a45fe624b9f72d4e6db672e51
- code/scales-projections/scales-comparison.py: 32a4582bba4a189f812e502420c7df9a5f03e95a45ef26528d3211f053b6e2b8
- code/showcases/windmap.py: 865d04b7e92fca51bc7bb1042cc7c3ae57cf71ffde47c6c6fed4cdbc54b36541
- code/threed/bunny.py: 2b63d1412ed7428562fdc6f52957a387f682af8ba8b72044eaaf0b3cfcee39a2
- code/typography/typography-legibility.py: 1ed37506df014ac66d6cf3d304ed8e2ee2183fac08e83ebc5d9c741a1bdd4f65
- code/typography/typography-math-stacks.py: ef0e1f387f905d4ef7ac76913c1e5bcacd689b2dbec195a39a0bc0eb173caaa7
- code/unsorted/3d/glm.py: c4ec2e29d13011cf05d3a1ff4473735111ec0c99a800a23bf14268b66e0a9a70
- code/unsorted/3d/plot.py: 7069dd6b909c1d78f7dabfa35de8050bae6d4c73c65e0a559ea3449e513bb3d3
- rst/00-preface.rst: 80408823efbde9fc6c65116840a34653d80aabf57d104622d6acde839e3878da
- rst/anatomy.rst: 9f74ed1ce3b95b62ae1af7a2f3d2d135004e9e60c96251779e6df21a5399ac94
- rst/animation.rst: cce103463c480a4609e0aaba347b2a9a97a2faddb72c6fcf2638c44f32e1109e
- rst/colors.rst: cbdc92ca71b07e1aeb6bcfdebea21bee2c278ef34f00e753472c3829dcc67aff
- rst/coordinates.rst: 706afa8f69b132c1bfebb8aba86c20e957281ad01caadb2706924a4c1c4c64af
- rst/defaults.rst: 73a9d77bf2b10301ec11f54e5f88daa715f78edee3992e36c6f53db47ebff430
- rst/layout.rst: 90e32ad05a89f7c093f24ed30d295abacb025dab9b43d7b50ff11edb312056ff
- rst/optimization.rst: 42a50f20a55752d6841645bc55b52b5d2e073e3b01d77aa5482079c7f30a2622
- rst/ornaments.rst: 6ad931e21fec57267577b939741793f07c33f2222987971ee3a18c883bfac840
- rst/projections.rst: bbf489d1552945b627034f4117438077cdd68911447fb84777436799f2020f03
- rst/rules.rst: 0f6cc05016bdf245c3cce714e4b9aab0c089f3b5cc0bb142650dd57cbce841ea
- rst/threed.rst: f536c97324f5689669df634ad56987263bc3c3e369f8cd508a7ab79d8c8542f7
- rst/typography.rst: a187534549ec533aa2df5e4b46e789e55cf2fa6b074e792e52ce08e33d385fe4
