# 移植排错、已知问题与可选动画

静态证据、未验证兼容性和新增工程处理分开记录；不把“可解析”写成“运行通过”。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## B01 · 按环境、资源、接口、输出分层排错

**描述与目的**：先定位失败阶段，再做最小复现。

**适用条件**：旧教学脚本在当前机器运行失败或输出不符。

**输入要求**：目标解释器、包版本、输入路径、字体、后端、预期输出。

**推荐实现**：检查外部素材和本地模块；离屏绘图在导入pyplot前选择Agg；使用独立输出目录。API版本疑点待后续实际验证。

**关键参数**：backend、字体解析路径、CWD、输出命名；避免直接运行原构建安装脚本。

**常见错误**：把语法解析当运行成功；把现有PDF当本次复现；未经允许安装依赖；所有异常都归咎于版本。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
import matplotlib
matplotlib.use("Agg")  # 独立无窗口进程，必须先于pyplot导入
import matplotlib.pyplot as plt
print(matplotlib.__version__, matplotlib.get_backend())
```

**证据与改编边界**：诊断顺序与隔离输出属于工程建议；本阶段未执行此诊断片段。

**原始出处**：

- [rst/anatomy.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/anatomy.rst#L158-L243)，L158–L243。
- [code/defaults/defaults-step-4.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/defaults/defaults-step-4.py#L11-L20)，L11–L20。
- [code/threed/bunny.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/threed/bunny.py#L80-L96)，L80–L96。

## B02 · 零值参数与逐面属性不能用隐式替换

**描述与目的**：有效零边界与颜色数组应保留调用者含义。

**适用条件**：适配color-wheel或自定义3D绘制函数时。

**输入要求**：边界可为0或None；逐面颜色数组与面数一致。

**推荐实现**：只用is None判断缺省；裁剪面时分别重排facecolor与edgecolor；尊重传入cmap。

**关键参数**：vmin/vmax、front/back索引、cmap；改动后需用边界值和不同颜色输入测试。

**常见错误**：vmin or min(data)吞掉0；把edgecolor赋给facecolor；接受cmap参数却总画magma。

**依赖**：输入为提供min/max方法的数组；通常NumPy

**代码配方（适配版）**：

```python
def resolve_bounds(data, vmin=None, vmax=None):
    if vmin is None:
        vmin = data.min()
    if vmax is None:
        vmax = data.max()
    return vmin, vmax
```

**证据与改编边界**：提出最小修正规则；未改原文件、未声明修复已通过。3D矩阵非对称投影另待数值验证。

**原始出处**：

- [code/colors/color-wheel.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/colors/color-wheel.py#L29-L41)，L29–L41。
- [code/unsorted/3d/plot.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/unsorted/3d/plot.py#L245-L265)，L245–L265。


动画末帧与编码器见 [animation.md](animation.md)。
