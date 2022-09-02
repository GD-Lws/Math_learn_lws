# % matplotlib inline
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import networkx as nx
from math import sqrt
import copy

data_1 = pd.read_excel('Data_1.xlsx')
data_2 = pd.read_excel('Data_2.xlsx')
data_1_len = len(data_1)
data_2_len = len(data_1)

# 垂直校准（垂直最大误差， 水平最大误差），水平校准（垂直最大误差， 水平最大误差），按规划前行最小误差，单位误差
data_1_param = [25, 15, 20, 25, 30, 0.001]
data_2_param = [20, 10, 15, 20, 20, 0.001]

data_1_A_x = data_1.iloc[0, 1]
data_1_A_y = data_1.iloc[0, 2]
data_1_A_z = data_1.iloc[0, 3]

data_1_B_x = data_1.iloc[data_1_len - 1, 1]
data_1_B_y = data_1.iloc[data_1_len - 1, 2]
data_1_B_z = data_1.iloc[data_1_len - 1, 3]

data_1_start_end_x = [data_1_A_x, data_1_B_x]
data_1_start_end_y = [data_1_A_y, data_1_B_y]
data_1_start_end_z = [data_1_A_z, data_1_B_z]

data_1_point_x = data_1.iloc[:, 1].to_list()
data_1_point_y = data_1.iloc[:, 2].to_list()
data_1_point_z = data_1.iloc[:, 3].to_list()
# data_1 vec(1) hor(0)
data_1_vec_hor = data_1.groupby(by='Type')
data_1_hor = data_1_vec_hor.get_group(0)
data_1_vec = data_1_vec_hor.get_group(1)

data_1_vec_x = data_1_vec.iloc[:, 1].to_list()
data_1_vec_y = data_1_vec.iloc[:, 2].to_list()
data_1_vec_z = data_1_vec.iloc[:, 3].to_list()
data_1_vec_index = data_1_vec.iloc[:, 0].to_list()

data_1_hor_x = data_1_hor.iloc[:, 1].to_list()
data_1_hor_y = data_1_hor.iloc[:, 2].to_list()
data_1_hor_z = data_1_hor.iloc[:, 3].to_list()
data_1_hor_index = data_1_hor.iloc[:, 0].to_list()

a_b_string = ['A', 'B']


# fig = plt.figure(figsize=(10, 10), dpi=100)
# # 创建3d绘图区域
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# ax.scatter3D(data_1_start_end_x, data_1_start_end_y, data_1_start_end_z, c='black')
# ax.scatter3D(data_1_vec_x, data_1_vec_y, data_1_vec_z, c='red')
# ax.scatter3D(data_1_hor_x, data_1_hor_y, data_1_hor_z, c='blue')
#
# for i in range(0, len(a_b_string)):
#     ax.text(data_1_start_end_x[i], data_1_start_end_y[i], data_1_start_end_z[i], a_b_string[i])
# ax.set_title('Data_1 plot')
# ax.plot3D(data_1_start_end_x, data_1_start_end_y, data_1_start_end_z, 'gray')
# plt.show()


# 距离计算公式
def point_point_distance(x_1, y_1, z_1, x_2, y_2, z_2):
    p_p_distance = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2)
    return p_p_distance


def data_distance(index_0, index_1):
    temp_distance = point_point_distance(data_1_point_x[index_0], data_1_point_y[index_0], data_1_point_z[index_0],
                                         data_1_point_x[index_1], data_1_point_y[index_1], data_1_point_z[index_1])
    return temp_distance


data_1_mat = np.zeros((data_1_len, data_1_len))
data_1_graph = np.zeros((data_1_len, data_1_len))

data_inf = np.Inf

# 上三角矩阵
for i in range(0, data_1_len):
    for j in range(i, data_1_len):
        if i == j:
            data_1_mat[i][j] = data_inf
            data_1_graph[i][j] = 0
        # 同属于一个校正组
        elif i in data_1_hor_index and j in data_1_hor_index:
            data_1_mat[i][j] = data_inf
            data_1_graph[i][j] = 0
        elif i in data_1_vec_index and j in data_1_vec_index:
            data_1_mat[i][j] = data_inf
            data_1_graph[i][j] = 0
        else:
            dist = data_distance(i, j)
            if dist * data_1_param[-1] >= data_1_param[-2]:
                data_1_mat[i][j] = data_inf
                data_1_graph[i][j] = 0
            else:
                data_1_mat[i][j] = dist
                data_1_graph[i][j] = dist
# print(data_1_graph)

data_1_mat_T = data_1_mat.T
# 距离的邻接矩阵
data_1_mat_dist = data_1_mat + data_1_mat_T
data_1_mat_dist_2 = copy.copy(data_1_mat_dist)

# 距离筛选
for i in range(0, data_1_len):
    for j in range(0, data_1_len):
        # 失衡飞行
        if data_1_mat_dist[i][j] * data_1_param[-1] >= data_1_param[-2]:
            data_1_mat_dist_2[i][j] = data_inf
        # j 为垂直校正点
        elif j in data_1_vec_index:
            if data_1_mat_dist[i][j] * data_1_param[-1] > data_1_param[0] or data_1_mat_dist[i][j] * data_1_param[-1] > \
                    data_1_param[1]:
                data_1_mat_dist_2[i][j] = data_inf
        # j 为水平校正点
        elif j in data_1_hor_index:
            if data_1_mat_dist[i][j] * data_1_param[-1] > data_1_param[3] or data_1_mat_dist[i][j] * data_1_param[-1] > \
                    data_1_param[2]:
                data_1_mat_dist_2[i][j] = data_inf

print(data_1_mat_dist_2[0][503] + data_1_mat_dist_2[503][69] < data_1_mat_dist_2[0][69])

data_1_vec_buff_2 = [0] * data_1_len
data_1_hor_buff_2 = [0] * data_1_len

for i in range(0, data_1_len):
    if i in data_1_vec_index:
        data_1_vec_buff_2[i] = 0
        data_1_hor_buff_2[i] = data_1_mat_dist_2[0][i] * data_1_param[-1]
    elif i in data_1_hor_index:
        data_1_vec_buff_2[i] = data_1_mat_dist_2[0][i] * data_1_param[-1]
        data_1_hor_buff_2[i] = 0
    else:
        data_1_vec_buff_2[i] = data_1_mat_dist_2[0][i] * data_1_param[-1]
        data_1_hor_buff_2[i] = data_1_mat_dist_2[0][i] * data_1_param[-1]


def dijkstra(matrix, start_point, end_point):
    global data_1_vec_buff_2, data_1_hor_buff_2, data_1_vec_index, data_1_hor_index
    matrix_len = len(matrix)
    path_array = []  # 用于保存路径
    temp_array = []  # 用于复制
    path_array.extend(matrix[start_point])
    temp_array.extend(matrix[start_point])

    # 从start_point点经过路径，到达该点的误差
    path_vec_array = copy.copy(data_1_vec_buff_2)
    path_hor_array = copy.copy(data_1_hor_buff_2)

    temp_array[start_point] = data_inf  # 处理过得节点变成inf, 表示不是最小权值的节点
    visited = [start_point]  # 用于保存处理过得节点
    path_parent = [start_point] * matrix_len  # 初始父节点都为start_point

    while len(visited) < matrix_len:
        i = temp_array.index(min(temp_array))  # 从最近开始寻找
        temp_array[i] = data_inf  # 已处理变为inf
        path = [str(i)]  # 用于画路径
        k = i
        t = 0
        while path_parent[k] != start_point:  # 找该节点的父节点添加到path，直到父节点是start
            path.append(str(path_parent[k]))
            k = path_parent[k]
            t = t + 1
        path.append(str(start_point))
        path.reverse()  # path反序产生路径
        print(str(i) + ':', '->'.join(path))
        visited.append(i)  # 该索引已经处理了
        if i == end_point:
            print("end_point_vec_buff: " + str(path_vec_array[end_point]))
            print("end_point_hor_buff: " + str(path_hor_array[end_point]))
            print("612_vec_buff: " + str(path_vec_array[612]))
            print("612_hor_buff: " + str(path_hor_array[612]))
            print("point_num: ", t)
            return path_array
        for j in range(matrix_len):
            if j not in visited and t < 9:
                # 当前点的距离到j点距离，比现有0点到j点的最近距离还要小
                if path_array[i] + matrix[i][j] < path_array[j]:
                    vec_buff_temp = path_vec_array[i] + matrix[i][j] * data_1_param[-1]
                    hor_buff_temp = path_hor_array[i] + matrix[i][j] * data_1_param[-1]
                    if j in data_1_vec_index and vec_buff_temp <= data_1_param[0] and hor_buff_temp <= data_1_param[1]:
                        path_vec_array[j] = 0
                        path_hor_array[j] = hor_buff_temp
                        path_array[j] = temp_array[j] = path_array[i] + matrix[i][j]
                        path_parent[j] = i  # 说明父节点是i
                    elif j in data_1_hor_index and vec_buff_temp <= data_1_param[2] and hor_buff_temp <= data_1_param[
                        3]:
                        path_vec_array[j] = vec_buff_temp
                        path_hor_array[j] = 0
                        path_array[j] = temp_array[j] = path_array[i] + matrix[i][j]
                        path_parent[j] = i  # 说明父节点是i
                    elif j == 612 and vec_buff_temp <= data_1_param[-2] and hor_buff_temp <= data_1_param[-2]:
                        path_array[j] = temp_array[j] = path_array[i] + matrix[i][j]
                        path_parent[j] = i  # 说明父节点是i
                        path_vec_array[j] = vec_buff_temp
                        path_hor_array[j] = hor_buff_temp
    return path_array


print(dijkstra(data_1_mat_dist_2, 0, 612))

answer = data_1_mat_dist_2[0][503] + data_1_mat_dist_2[503][69] + data_1_mat_dist_2[69][237] + \
         data_1_mat_dist_2[237][155] + data_1_mat_dist_2[155][338] + data_1_mat_dist_2[338][457] + \
         data_1_mat_dist_2[457][555] + data_1_mat_dist_2[555][436] + data_1_mat_dist_2[436][612]
print("answer")
print(answer)

answer_2 = data_1_mat_dist_2[0][503] + data_1_mat_dist_2[503][294] + data_1_mat_dist_2[294][91] + \
           data_1_mat_dist_2[91][607] + data_1_mat_dist_2[607][170] + data_1_mat_dist_2[170][278] + \
           data_1_mat_dist_2[278][369] + data_1_mat_dist_2[369][214] + data_1_mat_dist_2[214][397] + \
           data_1_mat_dist_2[397][612]
print(answer_2)

# print(503 in data_1_vec_index)
# print(69 in data_1_hor_index)
# print(80 in data_1_hor_index)

# print((data_1_mat_dist_2[0][503] * data_1_param[-1]) <= data_1_param[0])
# print((data_1_mat_dist_2[0][503] * data_1_param[-1]) <= data_1_param[1])
#
# print(((data_1_mat_dist_2[0][503] + data_1_mat_dist_2[503][69]) * data_1_param[-1]))
# print(data_1_param[3])
# # 503 是垂直校正点，69是水平校正点
# # 水平
# print(((data_1_mat_dist_2[0][503] + data_1_mat_dist_2[503][69]) * data_1_param[-1]) <= data_1_param[3])
# # 垂直
# print((data_1_mat_dist_2[503][69] * data_1_param[-1]) <= data_1_param[2])
#
# print((data_1_mat_dist_2[0][503] * data_1_param[-1] + data_1_mat_dist_2[503][80] * data_1_param[-1]) <= data_1_param[3])
# print((data_1_mat_dist_2[503][80] * data_1_param[-1]) <= data_1_param[2])
