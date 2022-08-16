# 投资的收益和风险
# 市场上有n种资产si(i=12…n)可以选择，现用数额为M的相当大的资金作一个时期的投资这n种资产
# 在这一时期内购买sj的平均收益率为ri，风险损失率为qi，投资越分散，总的风险越少，
# 总体风险可用投资的si中最大的一个风险来度量

# 将多目标规划转化为一个目标的线性规划，分为三个模型
# (1) 固定风险水平，优化收益
# (2) 固定盈利水平，极小化风险
# (3) 两个目标函数加权求和

# 模型一：
import matplotlib.pyplot as plt
from numpy import ones, diag, c_, zeros
from scipy.optimize import linprog
import latex


# plt.rc('text',usetex=True); plt.rc('font',size=16)
# c = [-0.05,-0.27,-0.19,-0.185,-0.185]
# A = c_[zeros(4),diag([0.025,0.015,0.055,0.026])]
# Aeq =[[1,1.01,1.02,1.045,1.065]]; beq = [1]
# a=0; aa=[]; ss=[];
# while a<0.05:
#     b = ones(4)*a
#     res = linprog(c,A,b,Aeq,beq)
#     x = res.x; Q = -res.fun
#     aa.append(a); ss.append(Q) #把最优值都保存起来
#     a = a+0.001
# print(aa)


# 模型二
import pylab as plt
import numpy as np
import cvxpy as cp
plt.rc('text',usetex=True); plt.rc('font',size=16)
x=cp.Variable(6,pos=True)
obj=cp.Minimize(x[5])
a1=np.array([0.025, 0.015, 0.055, 0.026])
a2=np.array([0.05, 0.27, 0.19, 0.185, 0.185])
a3=np.array([1, 1.01, 1.02, 1.045, 1.065])
k=0.05; kk=[]; ss=[]
while k<0.27:
    con=[cp.multiply(a1,x[1:5])-x[5]<=0,
         a2@x[:-1]>=k, a3@x[:-1]==1]
    prob=cp.Problem(obj,con)
    prob.solve(solver='GLPK_MI')
    kk.append(k); ss.append(prob.value)
    k=k+0.005
plt.plot(kk,ss,'r*')
plt.xlabel('$k$'); plt.ylabel('$R$',rotation=90)
# plt.savefig('figure5_1_2.png',dpi=500);
plt.show()
