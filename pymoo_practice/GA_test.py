from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.problems import get_problem
from pymoo.optimize import minimize
import numpy as np

problem = get_problem("g1")

algorithm = GA(
    pop_size=100,
    eliminate_duplicates=True
)

res = minimize(problem, algorithm, seed=1, verbose=True)
# print(res.F)
# print(res.X)

xu=np.array([10, 5, 10])
print(xu)