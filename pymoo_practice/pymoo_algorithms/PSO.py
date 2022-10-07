from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.problems.single import Rastrigin

problem_pso = Rastrigin()

algorithm_pso = PSO()

res_pso = minimize(problem_pso,
                   algorithm_pso,
                   seed=1,
                   verbose=False)

print("Best solution found: \nX = %s\nF = %s" % (res_pso.X, res_pso.F))
