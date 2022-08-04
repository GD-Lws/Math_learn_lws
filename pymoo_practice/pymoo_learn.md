# Pymoo Learn
# 多目标优化
## 基本
- 变量类型（连续、离散/整数、二进制或排列） 
- 变量数
- 目标数量 
- 约束
- 多模态 （局部搜索的局限性） 
- 可区分性 
- 评估时间 
- 不确定性 （噪声）

## minimize函数
* problem：包含要解决的问题的问题对象  
* algorithm：表示要使用的算法的算法目标。
* termination：定义算法何时终止的终止对象或元组。如果未提供，将使用默认终止标准。我们故意将终止列为参数而不是选项。特定算法可能需要对终止进行一些改进才能可靠地工作。
* seed: 大多数算法都有一些随机性。将种子设置为正整数值可确保可重复的结果。如果未提供，将自动设置随机种子，并将使用的整数存储在Result对象中。
* verbose：布尔值，定义是否应在运行期间打印输出。
* display：您可以覆盖每次迭代中应该打印的输出。因此，自定义Display对象可用于自定义目的。
* save_history：一个布尔值，表示是否应在每次迭代中存储算法的快照。如果启用，Result对象将包含历史记录。
* return_least_infeasible：如果算法找不到可行解，是否应该返回最小不可行解。默认情况下False。、

## Termination Criterion
* 评判终止条件（可以多个条件）
* 基于评估次数（n_eval）
* 基于代数（n_gen）
* 基于时间（time）
* 设计空间公差(xtol)
* 目标空间容差(ftol)

## Display
* n_gen: 直到这一点的当前代数或迭代数。 
* n_eval: 到目前为止的功能评估次数。
* n_nds: 对于多目标问题，找到最优解的非支配数。
* cv(min): 当前总体中的最小约束违反 (CV)
* cv(avg): 当前总体的平均约束违反（CV）
* f_opt: 对于单目标问题，目前找到的最佳函数值。
* f_gap: 对于单目标问题，与最优值的最佳差距（仅在最优值已知时才打印）。
* eps/indicator: 对于多目标问题，指标（理想、最低点、f）在过去几代中的变化（仅在帕累托前沿未知时才打印）。如需更多信息，我们鼓励您查看相应的出版物（[27]，pdf）。 
* igd/gd/hv: 对于多目标问题，性能指标（仅在帕累托前沿已知时才打印）。

## Result
* res.X：设计空间值是
* res.F：目标空间值
* res.G: 约束值
* res.CV: 聚合约束违规
* res.algorithm: 被迭代的算法对象
* res.opt: 作为Population对象的解决方案。
* res.pop: 最终人口
* res.history: 算法的历史。（仅save_history在算法初始化期间启用）
* res.time：运行算法所需的时间

## Problem
### Problem参数
* n_var:表示设计变量数量的整数值。
* n_obj:表示目标数量的整数值。
* n_constr:表示约束数量的整数值。
* xl:表示设计变量下限的浮点数或np.ndarray长度。n_var
* xu:表示设计变量上限的浮点数或np.ndarray长度。n_var
* vtype:（可选）用户的类型提示应该优化什么变量。
### Problem定义
#### vector矢量化定义
* 这意味着在每一代中都会评估多个解决方案。这是实现函数评估并行化的理想选择。因此，问题的默认定义检索一组要评估的解决方案。实际的函数评估发生在该_evaluate方法中，该方法旨在out用相应的数据填充字典。 
#### ElementwiseProblem（loop）
#### FunctionProblem


## Result
* res.X：设计空间值是
* res.F：目标空间值
* res.G: 约束值
* res.CV: 聚合约束违规
* res.algorithm: 被迭代的算法对象
* res.opt: 作为Population对象的解决方案。
* res.pop: 最终人口
* res.history: 算法的历史。（仅save_history在算法初始化期间启用）
* res.time：运行算法所需的时间

## 定制化