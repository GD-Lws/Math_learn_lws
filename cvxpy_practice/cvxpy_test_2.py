# 指派问题
# 标准指派模型，拟分派n个人完成n想工作，每个人仅需一个去完成，求效率最高
# Q_1 问题
# G: min z = sum(sum(c*x))
# st： 0,1规划

import cvxpy as cp
import numpy as np

c = np.array([[4, 8, 7, 15, 12],
            [7, 9, 17, 14, 10],
            [6, 9, 12, 8, 7],
            [6, 7, 14, 6, 10],
            [6, 9, 12, 10, 6]])
x = cp.Variable((5,5),integer=True)
obj = cp.Minimize(cp.sum(cp.multiply(c,x)))
# 限制条件、0-1规划
con= [0 <= x, x <= 1, 
      cp.sum(x, axis=0, keepdims=True)==1,
      cp.sum(x, axis=1, keepdims=True)==1]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI')
print("最优值为:",prob.value)
print("最优解为：\n",x.value)


# 广泛指派模型，通常方法就是先转化为标准形式然后用匈牙利算法求解
# 最大化指派问题：，诸如利润、业绩效应等，可以将问题最大化转为（M - c）的最小化
# 人数和任务数不等的指派问题，那边少添加那边，虚拟人完成效率取0，虚拟任务完成效率取0
# 一个人可完成多项任务指派问题，可以把该人看作相同几个人来接受指派
# 某项任务一定不能由某人完成的指派问题，将响应的效率值取最大化