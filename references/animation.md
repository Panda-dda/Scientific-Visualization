# 动画与编码器

## B03 · 动画与编码器按需启用

**描述与目的**：更新已有Artist；交互帧间隔与视频帧率分别设置。

**适用条件**：需要动态过程演示；静态科学图不需要视频依赖。

**输入要求**：X,Y:(N,)有序序列；每帧索引0…N-1。

**推荐实现**：创建线对象后set_data；持有动画对象；MP4导出前单独检查FFmpeg。

**关键参数**：interval(ms)、fps、保存dpi、帧数；首尾数据点覆盖需明确。

**常见错误**：每帧新建整图；丢失动画对象引用；X[:frame]在最后一帧漏末点；把tqdm当加速器。

**依赖**：Matplotlib；MP4额外需要FFmpeg；tqdm仅用于可选进度显示

**代码配方（适配版）**：

```python
from matplotlib import animation

def animate_trace(fig, ax, x, y):
    line, = ax.plot([], [])
    def update(i):
        line.set_data(x[:i+1], y[:i+1])
        return (line,)
    return animation.FuncAnimation(fig, update, frames=len(x), interval=33)
# 调用前固定轴范围；MP4保存另需FFMpegWriter与可用FFmpeg。
```

**证据与改编边界**：由教材动画接口改写；:i+1是静态边界修正，未运行验证。动画是可选扩展，不是核心强制依赖。

**原始出处**：

- [rst/animation.rst](https://github.com/rougier/scientific-visualization-book/blob/62fa569f30333c817c13e4dc757877c1192fd15a/rst/animation.rst#L18-L91)，L18–L91。
