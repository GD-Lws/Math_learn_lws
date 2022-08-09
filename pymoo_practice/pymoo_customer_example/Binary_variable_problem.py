# 使用遗传算法，解决二元问题
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.operators.crossover.pntx import TwoPointCrossover
from pymoo.operators.mutation.bitflip import BitflipMutation
from pymoo.operators.sampling.rnd import BinaryRandomSampling
from pymoo.optimize import minimize
from pymoo.problems.single.knapsack import create_random_knapsack_problem

# 创建背包问题
problem = create_random_knapsack_problem(30)

algorithm = GA(
    pop_size=200,
    # 二进制随机
    sampling=BinaryRandomSampling(),
    # 两点交叉
    crossover=TwoPointCrossover(),
    # 位翻转突变
    mutation=BitflipMutation(),
    eliminate_duplicates=True)

res = minimize(problem,
               algorithm,
               ('n_gen', 100),
               verbose=False)

print("Best solution found: %s" % res.X.astype(int))
print("Function value: %s" % res.F)
print("Constraint violation: %s" % res.CV)