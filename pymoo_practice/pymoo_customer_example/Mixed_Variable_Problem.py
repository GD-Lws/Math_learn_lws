# 混合变量问题
# 对于该情况，必须将不同的进化算子应用于不同类型的变量
# 通过设置值得MixedVariableProblem位置来支持这一点vars

from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice, Binary
from pymoo.core.mixed import MixedVariableGA
from pymoo.core.variable import Real, Integer
from pymoo.optimize import minimize


class MixedVariableProblem(ElementwiseProblem):

    def __init__(self, **kwargs):
        vars = {
            "b": Binary(),
            "x": Choice(options=["nothing", "multiply"]),
            "y": Integer(bounds=(0, 2)),
            "z": Real(bounds=(0, 5)),
        }
        super().__init__(vars=vars, n_obj=1, **kwargs)

    def _evaluate(self, X, out, *args, **kwargs):
        b, x, z, y = X["b"], X["x"], X["z"], X["y"]

        f = z + y
        if b:
            f = 100 * f

        if x == "multiply":
            f = 10 * f

        out["F"] = f


problem = MixedVariableProblem()

algorithm = MixedVariableGA(pop=10)

res = minimize(problem,
               algorithm,
               termination=('n_evals', 1000),
               seed=1,
               verbose=False)

print("Best solution found: \nX = %s\nF = %s" % (res.X, res.F))