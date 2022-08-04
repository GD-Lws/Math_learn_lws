# TSP问题：路程最短
# 变量：目标点的排序编号
# 优化方向：使得路程最短

import numpy as np
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.optimize import minimize
from pymoo.termination import get_termination
import matplotlib.pyplot as plt

a = np.loadtxt("Pdata17_2.txt")
xy, d = a[:, :2], a[:, 2:]
N = len(xy)

class TSP_Problem(Problem):
    def __init__(self):

        super().__init__(
            # 一共有102个变量（代表序号）
            n_var=102,
            # 目标函数一个
            n_obj=1,
            # 约束值为1
            n_ieq_constr=1,
            # 最小值为0
            xl=0.0,
            # 最大值为1
            xu=102.0
        )

    def _evaluate(self, x, out, *args, **kwargs):

