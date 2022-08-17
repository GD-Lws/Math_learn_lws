# Matplotlib
## 画图专用
## 官方教程 https://matplotlib.org/stable/gallery/lines_bars_and_markers/index.html

| 类型 | 函数 | 作用 | 所在文件 |
| :--- | :---: | :--: | :---:|
| 折线图 | plt.plot() | （每天的利润额变化情况） | test_0 |
| 柱形图 | plt.bar() | （显示区域性差异） | test_0 |
| 直方图图 | plt.hist() | 用于概率分布（每天的利润额） | test_0 |
| 饼图 | plt.pie() | 用于显示占总和的百分比（不同类型商品的销售额差异） | test_0 |
| 散点图 | plt.scatter() | 反映一个变量受另外一个变量的影响程度（销售额与利润额两者的关系） | test_1 |
| 箱形图 | plt.boxplot() | 显示出一组数据中的最大值、最小值、中位数、及上下四分卫数 | test_1 |
| 等高线图 | plt.contour()绘制等高线; plt.contourf()填充等高线 | 查看因变量Z与自变量X，Y之间的函数图像变化 | test_1 |
| 小提琴图 | plt.violinplot() | 展示数据分布状态以及概率密度的图表 | test_1 |
| 矢量图 | plt.quiver() | |
| 极轴图 | 更改y轴 2*np.pi |  |
| 树形图 | squarify.plot(sizes, color = colors) | 适合展示层次关系，体现同级之间的数据比较(产品是否具有差异性) |
| 热力图 | sns.heatmap() | |
| 甘特图 |  | 时间安排 |
| 自相关图 | plot_acf(), plot_pacf() | |



## 图形参数
* linestyle = '-' 线样式
* color = 'red' 颜色
* linewidth = 5.0 线宽
* marker = '*' 点样式
* plt.xlabel()给x轴加标签；plt.ylabel()给y轴加标签
* plt.ylim()x轴的刻度，
* plt.legend()图例
* plt.grid()网格线