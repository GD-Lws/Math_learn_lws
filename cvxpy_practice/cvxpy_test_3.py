# 整数规划--装箱问题
# Q_2
# 包装箱总重为89T，而载重只有80T，因此需要多装，
# 约束条件：总件数小于7
# 总长度
# 重量限制
# 特殊限制
# 目标函数
# 总厚度最大
import cvxpy as cp
import numpy as np
L = np.array([48.7,52.0,61.3,72.0,48.7,52.0,64.0])
w = np.array([2000,3000,1000,500,4000,2000,1000])
a = np.array([8,7,9,6,6,4,8])
x = cp.Variable((2,7), integer=True)
# 总厚度最大
obj = cp.Maximize(cp.sum(x * L))
# 总重量最大
# obj = cp.Maximize(cp.sum(x * w))

con = [ cp.sum(x,axis=0,keepdims=True) <= a.reshape(1,7),
        x*L <= 1020,
        x*w <= 40000,
        cp.sum(x[:,4:]*L[4:]) <= 302.7,
        x >= 0]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI',verbose =True)
print("最优值为:",prob.value)
print("最优解为：\n",x.value)