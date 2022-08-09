# 有偏初始化
# 定制算法的一种方法是有偏差的初始总体。
# 如果专家知识已经存在，这将非常有帮助，
# 并且应该改进已知的解决方案。
# 在下文中，提供了两种不同的初始化方式：
# a）只提供变量的设计空间；b）提供了目标和约束的Population对象，不需要再次计算


import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.core.evaluator import Evaluator
from pymoo.core.population import Population
from pymoo.optimize import minimize

problem_0 = get_problem("zdt2")

X = np.random.random((300, problem_0.n_var))

algorithm_0 = NSGA2(pop_size=100, sampling=X)

minimize(problem_0,
         algorithm_0,
         ('n_gen', 10),
         seed=1,
         verbose=True)

problem = get_problem("zdt2")

# create initial data and set to the population object
X = np.random.random((300, problem.n_var))
pop = Population.new("X", X)
Evaluator().eval(problem, pop)

algorithm = NSGA2(pop_size=100, sampling=pop)

minimize(problem,
         algorithm,
         ('n_gen', 10),
         seed=1,
         verbose=True)
