import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.optimize import minimize
from pymoo.core.crossover import Crossover
from pymoo.core.mutation import Mutation
from pymoo.core.sampling import Sampling


# 子集选择问题
# L为奖励集，定义的变量长度为L的长度，通过改变是否选择来求和
class SubsetProblem(ElementwiseProblem):
    def __init__(self,
                 L,
                 n_max
                 ):
        super().__init__(n_var=len(L), n_obj=1, n_ieq_constr=1)
        self.L = L
        self.n_max = n_max

    def _evaluate(self, x, out, *args, **kwargs):
        # 使得L总和最小
        out["F"] = np.sum(self.L[x])
        # 限制条件,使数量为10,x为布尔值
        out["G"] = (self.n_max - np.sum(x)) ** 2


# create the actual problem to be solved
np.random.seed(1)
# 随机生成L
L = np.array([np.random.randint(100) for _ in range(100)])
Award_array = np.random.randint(30, 120, size=(20, 5))
Test_array = Award_array.flatten()
n_max = 5
problem = SubsetProblem(Test_array, n_max)


class MySampling(Sampling):
    def _do(self, problem, n_samples, **kwargs):
        X = np.full((n_samples, problem.n_var), False, dtype=bool)

        for k in range(n_samples):
            # 随机产生序列，先产生
            I = np.random.permutation(problem.n_var)[:problem.n_max]
            X[k, I] = True
        return X


class BinaryCrossover(Crossover):
    def __init__(self):
        super().__init__(2, 1)

    # n_parents, 即是父辈
    def _do(self, problem, X, **kwargs):
        n_parents, n_matings, n_var = X.shape

        _X = np.full((self.n_offsprings, n_matings, problem.n_var), False)

        for k in range(n_matings):
            p1, p2 = X[0, k], X[1, k]
            # 逐个元素与运算
            both_are_true = np.logical_and(p1, p2)
            _X[0, k, both_are_true] = True

            n_remaining = problem.n_max - np.sum(both_are_true)

            I = np.where(np.logical_xor(p1, p2))[0]

            S = I[np.random.permutation(len(I))][:n_remaining]
            _X[0, k, S] = True

        return _X


class MyMutation(Mutation):
    def _do(self, problem, X, **kwargs):
        for i in range(X.shape[0]):
            X[i, :] = X[i, :]
            is_false = np.where(np.logical_not(X[i, :]))[0]
            is_true = np.where(X[i, :])[0]
            X[i, np.random.choice(is_false)] = True
            X[i, np.random.choice(is_true)] = False

        return X


algorithm = GA(
    pop_size=100,
    sampling=MySampling(),
    crossover=BinaryCrossover(),
    mutation=MyMutation(),
    eliminate_duplicates=True)

res = minimize(problem,
               algorithm,
               ('n_gen', 90),
               seed=1,
               verbose=True)

print(Test_array)
print("Function value: %s" % res.F[0])
print("Subset:", np.where(res.X)[0])
print(Test_array[np.where(res.X)[0]])
