#导入可视化分析相关的包
import matplotlib.pyplot as plt

#用来正常显示中文标签和负号
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#数据设置
x =['中南','东北','华东','华北','西南','西北'];
y1=[223.65, 488.28, 673.34, 870.95, 1027.34, 1193.34];
y2=[214.71, 445.66, 627.11, 800.73, 956.88, 1090.24];

#设置输出的图片大小
figsize = 10,8
figure, ax = plt.subplots(figsize=figsize)

#在同一幅图片上画两条折线
A,=plt.plot(x,y1,'-r',label='2019年销售额',linewidth=5.0)
B,=plt.plot(x,y2,'b-.',label='2018年销售额',linewidth=5.0)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('SimHei') for label in labels]

#设置图例并且设置图例的字体及大小
font1 = {'family' : 'SimHei','weight' : 'normal','size' : 15,}
legend = plt.legend(handles=[A,B],prop=font1)

#设置横纵坐标的名称以及对应字体格式
font2 = {'family' : 'SimHei','weight' : 'normal','size' : 20,}
plt.xlabel('地区',font2)
plt.ylabel('销售额',font2)

#输出图形
plt.show()



