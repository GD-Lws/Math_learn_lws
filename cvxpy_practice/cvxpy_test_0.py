# 求解一般线性规划
# 要注意将不等式化成标准形
# 就是求min和小等于号

import numpy
from cvxopt import matrix, solvers

# 目标函数
c = matrix([2.,1]);
# s.t. 限制函数左侧
A = matrix([[-1.,1], [-1,-1], [1,-2], [0,-1]])
# 限制函数右侧
b = matrix([1., -2, 4, 0]); 
#  等式
Aeq = matrix([1.,2],(1,2)) #Aeq为行向量
beq = matrix(3.5);
sol=solvers.lp(c, A, b, Aeq, beq)
print("最优解为：\n",sol['x'])
print("最优值为：",sol['primal objective'])
