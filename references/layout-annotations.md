# 坐标定位、标签与放大

多面板网格见 multi-panel.md；这里处理单个标注与轴的关系。

> 来源：Nicolas P. Rougier；中文提炼与参数化改编，2026-11-06。短配方不等同完整验证程序；可运行例子与已测范围见 [README](../README.md)，出处与许可见 [SOURCE_MAP](../SOURCE_MAP.md)。

## L01 · 区分数据坐标、轴比例和物理偏移

**描述与目的**：数据点位置、轴框位置和固定纸面距离由不同变换控制。

**适用条件**：面板字母、轴边说明、固定距离标签。

**输入要求**：ax/fig；文字；锚点坐标；偏移 point。

**推荐实现**：轴比例锚点使用 transAxes；物理偏移通过 point/72 转英寸再用 dpi_scale_trans；数据位置使用 transData。

**关键参数**：transform、ScaledTranslation；混合坐标适用于已理解的投影，不默认扩展至任意投影。

**常见错误**：把10/72英寸称为10像素；遗漏 transform；把横纵轴比例偏移当作相等物理距离。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from matplotlib.transforms import ScaledTranslation

def panel_label(ax, label, offset_pt=10):
    off = ScaledTranslation(offset_pt/72, offset_pt/72,
                            ax.figure.dpi_scale_trans)
    return ax.text(0, 0, label, transform=ax.transAxes + off)
```

**证据与改编边界**：参数化原面板字母示例，明确偏移单位为 point。

**原始出处**：

- [rst/coordinates.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/coordinates.rst#L19-L37)，L19–L37。
- [rst/coordinates.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/coordinates.rst#L130-L171)，L130–L171。
- [code/coordinates/transforms-letter.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/coordinates/transforms-letter.py#L24-L36)，L24–L36。

## L02 · 直接标签减少曲线与图例的往返查找

**描述与目的**：曲线较少且标签可排开时，可在曲线附近写名称。

**适用条件**：少量曲线，末端或局部锚点可辨。

**输入要求**：x,y:(N,),N>0；曲线对象与名称；预留标签空间。

**推荐实现**：让文字颜色与线对应；优先稳定锚点；标注拥挤时换位置、恢复图例或拆图。

**关键参数**：ha、va、textcoords、bbox；固定旋转角和索引不能照搬。

**常见错误**：端点重合；文本超出边界被裁切；标签遮挡关键拐点；在任意曲线上复用原示例固定角度。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
def label_endpoint(ax, x, y, line, name):
    return ax.annotate(name, xy=(x[-1], y[-1]), xytext=(4, 0),
                       textcoords="offset points", va="center",
                       color=line.get_color())
```

**证据与改编边界**：把源码固定索引改为末端索引，并使用物理偏移；不能保证任意数据标签无重叠。

**原始出处**：

- [rst/ornaments.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/ornaments.rst#L70-L83)，L70–L83。
- [code/ornaments/legend-alternatives.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/legend-alternatives.py#L35-L106)，L35–L106。

## L03 · 放大图保持数据与空间对应

**描述与目的**：放大同一数据子区域并连接到全局图。

**适用条件**：拥挤局部需要细节，同时必须保留整体上下文。

**输入要求**：X,Y:(N,)；中心(x,y)，半宽dx、半高dy均>0；主轴与小轴。

**推荐实现**：小轴绘制同一数据，仅改变范围；主图框出区域，用 ConnectionPatch 连接对应边界。

**关键参数**：coordsA/coordsB、xlim/ylim、连接点；多个局部图按空间顺序排。

**常见错误**：用不同数据重绘局部；坐标系混用；把随机挑选的演示中心称为异常检测。

**依赖**：Matplotlib

**代码配方（适配版）**：

```python
from matplotlib.patches import Rectangle, ConnectionPatch

def connect_zoom(ax, inset, x, y, dx, dy):
    rect = Rectangle((x-dx, y-dy), 2*dx, 2*dy, fill=False)
    ax.add_patch(rect)
    inset.set(xlim=(x-dx, x+dx), ylim=(y-dy, y+dy))
    link = ConnectionPatch(xyA=(x+dx, y), xyB=(0, .5),
                           coordsA=ax.transData, coordsB=inset.transAxes)
    ax.figure.add_artist(link)
    return rect, link
```

**证据与改编边界**：仅封装区域和连接；调用方须在两轴绘制同一数据。布局位置需与所选连接边一致。

**原始出处**：

- [code/ornaments/annotation-zoom.py](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/code/ornaments/annotation-zoom.py#L15-L79)，L15–L79。
- [rst/ornaments.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/ornaments.rst#L195-L205)，L195–L205。
