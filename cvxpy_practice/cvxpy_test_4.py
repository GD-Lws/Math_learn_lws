# have problem
# 非线性规划模型
# 无约束和有约束讨论    
# 二次规划即目标函数为决策向量x的二次函数，约束条件又全安慰线性的

import cvxpy as cp
import numpy as np
c1 = np.array([1, 1, 3, 4, 2])
c2 = np.array([-8, -2, -3, -1, -2])
a = np.array([[1, 1, 1, 1, 1], [1, 2, 2, 1, 6], [2, 1, 6, 0, 0], [0, 0, 1, 1, 5]])
b = np.array([400, 800, 200, 200])
x = cp.Variable(5,integer=True)
obj = cp.Minimize(c1*x**2+c2*x)
con=[0<=x, x<=99, a*x<=b]
prob = cp.Problem(obj, con)
prob.solve(solver='SCIPY',verbose =True)
print("最优值为:",prob.value)
print("最优解为：\n",x.value)