from pymoo.algorithms.soo.nonconvex.optuna import Optuna
from pymoo.core.variable import Real, Integer
from pymoo.optimize import minimize

from pymoo_practice.pymoo_customer_example.Mixed_Variable_Problem import MixedVariableProblem

problem = MixedVariableProblem()

algorithm = Optuna()

res = minimize(problem,
               algorithm,
               termination=('n_evals', 300),
               seed=1,
               verbose=False)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))