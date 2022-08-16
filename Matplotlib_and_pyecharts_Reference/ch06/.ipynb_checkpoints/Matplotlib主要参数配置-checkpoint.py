
#导入绘图相关模块
import matplotlib.pyplot as plt
import numpy as np

#生成数据
x = np.arange(0,20,1)
y1 = (x-9)**2 + 1
y2 = (x+5)**2 + 8

#绘制图形
plt.plot(x,y1)
plt.plot(x,y2)

#输出图形
plt.show()



#导入绘图相关模块
import matplotlib.pyplot as plt
import numpy as np

#生成数据
x = np.arange(0,20,1)
y1 = (x-9)**2 + 1
y2 = (x+5)**2 + 8

#设置线的颜色，线宽，样式
plt.plot(x,y1,linestyle='-.',color='red',linewidth=5.0)
#添加点，设置点的样式，颜色，大小
plt.plot(x,y2,marker='*',color='green',markersize=10)

#输出图形
plt.show()



#导入绘图相关模块
import matplotlib.pyplot as plt
import numpy as np

#生成数据并绘图
x = np.arange(0,20,1)
y1 = (x-9)**2 + 1
y2 = (x+5)**2 + 8

#设置线的颜色，线宽，样式
plt.plot(x,y1,linestyle='-.',color='red',linewidth=5.0)
#添加点，设置点的样式，颜色，大小
plt.plot(x,y2,marker='*',color='green',markersize=10)

#设置x轴的刻度
plt.xlim(0,20)

#设置y轴的刻度
plt.ylim(0,400)

#输出图形
plt.show()



#导入绘图相关模块
import matplotlib.pyplot as plt
import numpy as np

#生成数据并绘图
x = np.arange(0,20,1)
y1 = (x-9)**2 + 1
y2 = (x+5)**2 + 8

#设置线的颜色，线宽，样式
plt.plot(x,y1,linestyle='-.',color='red',linewidth=5.0)
#添加点，设置点的样式，颜色，大小
plt.plot(x,y2,marker='*',color='green',markersize=10)

#给x轴加上标签
plt.xlabel('x',size=15)

#给y轴加上标签
plt.ylabel('y',size=15,rotation=90,horizontalalignment='right',verticalalignment='center')

#设置x轴的刻度
plt.xlim(0,20)

#设置y轴的刻度
plt.ylim(0,400)

#输出图形
plt.show()



#导入绘图相关模块
import matplotlib.pyplot as plt
import numpy as np

#生成数据并绘图
x = np.arange(0,20,1)
y1 = (x-9)**2 + 1
y2 = (x+5)**2 + 8

#设置线的颜色，线宽，样式
plt.plot(x,y1,linestyle='-.',color='red',linewidth=5.0,label='convert A')
#添加点，设置点的样式，颜色，大小
plt.plot(x,y2,marker='*',color='green',markersize=10,label='convert B')

#给x轴加上标签
plt.xlabel('x',size=15)

#给y轴加上标签
plt.ylabel('y',size=15,rotation=90,horizontalalignment='right',verticalalignment='center')

#设置x轴的刻度
plt.xlim(0,20)
#设置y轴的刻度
plt.ylim(0,400)

#设置图例
#plt.legend()
plt.legend(labels=['A', 'B'],loc='upper left',fontsize=15)

#输出图形
plt.show()
