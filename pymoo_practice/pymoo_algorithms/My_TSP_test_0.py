# TSP问题：路程最短
# 变量：目标点的排序编号
# 优化方向：使得路程最短
from random import shuffle

import numpy as np
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.optimize import minimize
from pymoo.termination import get_termination
import matplotlib.pyplot as plt
from pymoo.core.sampling import Sampling

a = np.loadtxt("Pdata17_2.txt")
xy, d = a[:, :2], a[:, 2:]
N = len(xy)

class TSP_Problem(Problem):
    def __init__(self, D, num):
        super().__init__(
            # 一共有102个变量（代表序号）
            n_var=num,
            # 目标函数一个
            n_obj=1,
            # 约束数为1
            n_ieq_constr=1,
            # 最小值为0
            xl=0.0,
            # 最大值为1
            xu=102.0
        )
        self.D = D
        self.num = num

    # x 应该为 每个地点的顺序
    # def _evaluate(self, x, out, *args, **kwargs):
    #     # 目标函数
    #     out["F"] =


# 使用改良圈算法生成Sampling
class TSPSampling(Sampling):
    def _do(self, problem, n_samples, **kwargs):
        # 该problem是已定义好的
        N = len(problem.n_var)
        c = np.arange(1, N - 1)
        # 随机顺序
        shuffle(c)
        # 因为开头和返回必须是同一个点
        c1 = np.r_[0, c, 101]
        flag = 1
        while flag > 0:
            flag = 0
            # 改良圈的思路是：任意选路线中的两点，把两点中所有位置颠倒过来（即倒序），看倒序后的路线长度是否比之前短，如果变短就接受这个巡航路线，否则不接受，进行下一次选两点并进行倒序的操作。
            for m in np.arange(1, N - 3):
                for n in np.arange(m + 1, N - 2):
                    if d[c1[m], c1[n]] + d[c1[m + 1], c1[n + 1]] < \
                            d[c1[m], c1[m + 1]] + d[c1[n], c1[n + 1]]:
                        c1[m + 1:n + 1] = c1[n:m:-1]
                        flag = 1
        # 将排序的好的重新赋值
        # 例如排序好的顺序是31 ， 23 ....
        # c1[c1] = np.arrange(N) -> c1[31] = 0
        c1[c1] = np.arange(N)
        X = c1
        return X


# 交叉

# 变异