# 排序问题
# 每个整数值只出现一次
# TSP问题
import numpy as np
from pymoo.core.repair import Repair
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.optimize import minimize
from pymoo.problems.single.traveling_salesman import create_random_tsp_problem
from pymoo.operators.sampling.rnd import PermutationRandomSampling
from pymoo.operators.crossover.ox import OrderCrossover
from pymoo.operators.mutation.inversion import InversionMutation
from pymoo.termination.default import DefaultSingleObjectiveTermination
from pymoo.problems.single.traveling_salesman import visualize
import matplotlib.pyplot as plt


# 将随机生成的点进行校正，使其第一个为起点
class StartFromZeroRepair(Repair):
    def _do(self, problem, X, **kwargs):
        I = np.where(X == 0)[1]

        for k in range(len(X)):
            i = I[k]
            X[k] = np.concatenate([X[k, i:], X[k, :i]])

        return X


problem = create_random_tsp_problem(20, 10, seed=1)

algorithm = GA(
    pop_size=20,
    # 随机采样
    sampling=PermutationRandomSampling(),
    # 反转变异
    mutation=InversionMutation(),
    # 边缘交叉
    crossover=OrderCrossover(),
    repair=StartFromZeroRepair(),
    eliminate_duplicates=True
)

# if the algorithm did not improve the last 200 generations then it will terminate (and disable the max generations)
termination = DefaultSingleObjectiveTermination(period=200, n_max_gen=np.inf)

res = minimize(
    problem,
    algorithm,
    termination,
    verbose=True,
    seed=1,
)

print("Traveling Time:", np.round(res.F[0], 3))
print("Function Evaluations:", res.algorithm.evaluator.n_eval)

visualize(problem, res.X)
plt.show()

print("finish")
