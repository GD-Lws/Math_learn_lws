# 最短路及最短距离
# 旨在寻找图中两点之间最短路劲，优化问题可用
# 如管道铺设、线路安排、厂区布局
# Q_1为例，将每年费用构造成邻接矩阵
import numpy as np
import networkx as nx
import pylab as plt
p=[25,26,28,31]; a=[10,14,18,26]; r=[20,16,13,11];
b=np.zeros((5,5)); # 邻接矩阵（非数学上的邻接矩阵）初始化
for i in range(5):
    for j in range(i+1,5):
        b[i,j]=p[i] + np.sum(a[0:j-i] )- r[j-i-1]; #pi为第i年年初的购置减去使用到k年的维护费用，r为出售价格
print(b)
G = nx.DiGraph(b)
p = nx.dijkstra_path(G, source=0, target=4, weight='weight')  #求最短路径；
print("最短路径为:",np.array(p)+1)  #python下标从0开始
d = nx.dijkstra_path_length(G, 0, 4, weight='weight') #求最短距离
print("所求的费用最小值为：",d)
s = dict(zip(range(5),range(1,6))) #构造用于顶点标注的标号字典
plt.rc('font',size=16)
pos=nx.shell_layout(G)  #设置布局
w = nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,font_weight='bold',labels=s,node_color='r')
nx.draw_networkx_edge_labels(G , pos, edge_labels=w)
path_edges=list(zip(p,p[1:]))
nx.draw_networkx_edges(G,pos,edgelist=path_edges,
            edge_color='r',width=3)
# plt.savefig("figure10_9.png",pdi=500); 
plt.show()
