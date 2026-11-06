---
name: scientific-visualization
description: Create, refine, or review scientific figures using source-grounded Python/Matplotlib techniques. Use for scientific plotting, figure debugging, multi-panel layouts, 2D/3D visualization, or publication export; preserve the user's chosen plotting stack.
---

# Scientific Visualization

根据数据含义和目标版面生成、修改或审查科研图。方法来自 howToDraw；实现范围主要为 Python/Matplotlib。先保留用户已有工具和代码；其他技术栈可借用通用原则，但没有对应源码依据时不要宣称已提供该栈的实现。

### 工作流

1. **确认任务与输出。** 从请求和现有材料确定要表达的关系、数据单位、图型、目标尺寸/格式及需要生成、修改还是只审查。已有答案不重复询问；会改变数据含义的缺失信息再询问。只审查时输出有依据的问题，不擅自重绘或改数据。
2. **检查数据与现有代码。** 核对数组形状、列含义、时间顺序、缺失值和单位。区间须由用户提供SD/SE/CI定义；不把透明叠加或纹理颜色当统计量。生成的功能测试数据显式标为合成，不代替实验数据。
3. **选择方法并读取对应参考。** 按下方路由加载当前任务所需文档。已知图型无需遍读选型文档；复杂问题可以组合参考。只有证据不足或需追溯时再查SOURCE_MAP。
4. **生成或修改代码。** 先检查可用环境；缺依赖时报告，安装须获许可。参数化输入、输出、尺寸和随机种子；采用局部样式，保持数据处理与绘图可分辨。例子按需适配，不直接批量执行原教程；原始素材保持不变。
5. **应用视觉设计。** 按最终物理尺寸设置字号/线宽，颜色编码与量值语义一致；明确刻度、图例、坐标尺度和单位。尊重指定期刊要求，不把样式文件或600 DPI当成普适规范。
6. **执行与目视修订。** 在独立输出目录运行，查看实际生成图；检查裁切、重叠、字号、轴尺度、色标中心、多面板对齐和三维遮挡。根据具体问题修改并复查。不能查看图时写明未完成视觉检查。
7. **导出。** 由用户选择 PDF/SVG/PNG/PGF/TEX，只生成指定格式及必需配套文件；示例通过 `--formats tex` 等参数选择，省略时保持 PDF/SVG/PNG 默认值。TEX 输出可编译包装文件与 PGF，混合图还包含 PNG 配套文件；先检查 XeLaTeX，细节见导出参考。按请求保存物理尺寸；矢量文件中的栅格层仍需合适DPI。使用新文件名，覆盖已有结果需要明确授权；避免输出到教程或技能安装目录。
8. **验证与交付。** 报告生成代码、输入依据、环境、输出路径、运行结果、实际视觉观察及未完成项。语法通过、运行通过、目视通过分别记录；没有执行和检查就不能宣称图已成功完成。只审查任务不要求重新生成文件，但须说明观察依据。

### 按问题路由

| 问题 | 读取 |
|---|---|
| 编码真实性、区间/面积含义、可重复性 | [references/principles.md](references/principles.md) |
| 图型与颜色量值类型未定 | [references/chart-selection.md](references/chart-selection.md) |
| 字体、数学文字、文字对比度 | [references/typography.md](references/typography.md) |
| 配色、渐变、样式统一 | [references/colors-styling.md](references/colors-styling.md) |
| 注释位置、直接标签、局部放大 | [references/layout-annotations.md](references/layout-annotations.md) |
| 对数轴、等比例、线段集合 | [references/visualization-2d.md](references/visualization-2d.md) |
| 三维投影、网格、遮挡、轨迹原语 | [references/visualization-3d.md](references/visualization-3d.md) |
| 多面板或边际直方图 | [references/multi-panel.md](references/multi-panel.md) |
| 尺寸、PDF/SVG/PNG、局部栅格化 | [references/publication-export.md](references/publication-export.md) |
| 运行错误、路径、字体环境、兼容性 | [references/debugging.md](references/debugging.md) |
| 动画、视频、首末帧问题 | [references/animation.md](references/animation.md) |

基础曲线/散点参考 [examples/line_scatter.py](examples/line_scatter.py)；边际布局参考 [examples/marginal_panels.py](examples/marginal_panels.py)；三维网格参考 [examples/projected_mesh.py](examples/projected_mesh.py)；密集数据导出参考 [examples/mixed_export.py](examples/mixed_export.py)。复用例子时连同 [examples/_common.py](examples/_common.py) 一起读取；明确只移植需要的逻辑，避免引入不必要的依赖。

### 能力与证据边界

- 三维面深度排序是画家算法，不能保证交叉面和透明对象的任意遮挡正确。保留原物理单位，不把构图归一化坐标冒充实际长度。
- 编队轨迹、共识曲线可迁移基础原语；特征根稳定区域和统计推断需要任务本身提供定义与依据，不能从教材图形效果推导科学结论。
- [SOURCE_MAP.md](SOURCE_MAP.md)保存出处、技术ID、改编和许可；源库旧API和已知问题先查debugging。若要适配未覆盖的API，应另行核查官方依据并标注新增来源。
- 源码片段存在不等于当前环境运行通过；示例的已测版本以实际验证记录为准。

### 完成标准

生成/修改任务交付可复现代码和已存在的输出，附真实运行与目视检查状态。审查任务交付定位到图中位置或代码行的具体问题和改法。环境阻碍时交付可完成部分及阻碍，不填造验证结果。
