# GA遗传算法学习
| 遗传学概念 |           遗传算法概念           |     数学概念     | 
|:------|:--------------------------:|:------------:| 
| 个体    |          要处理的基本对象          |     可行解      | 
| 群体    |           个体的集合            |  被选定的一组可行解   | 
| 染色体   |          个体的表现形式           |    可行解的编码    |
| 基因    |          染色体中的元素           |    编码中的元素    |
| 基因位   |        某一基因在染色体中的位置        |  元素在编码中的位置   |
| 适应值   |        个体对于环境的适应程度         | 可行解所对应的适应函数值 | 
| 种群    |        选定的一组染色体或个体         |   选定的一组可行解   |
| 选择    |         从群体中选择优胜个体         | 保留或复制适应值大的个体 | 
| 交叉    | 一组染色体对应基因段的交换 | 根据交叉原则产生一组新解| 
| 交叉概率  |       染色体对应基因段交换的概率        | 一般为0.65~0.90 |
| 变异    |         染色体水平上基因变化         | 编码的某些元素被改变   | 
| 变异概率  |       染色体水平上基因变化的概率        | 一般为0.001~0.01| 
| 进化    |           适者生存             | 个体进行优胜劣汰的进化 适应函数值优的可行解| 

### 步骤
1. 初始化群体
2. 适应值评价，保存最优染色体
3. 选择
4. 交配
5. 变异
6. 重新评价适应值，更新最优染色体
7. 满足终止条件

### 解空间的编码
1. 把一个问题的可行解从它的解空间到算法处理的搜索空间的转化方法称为编码
2. 常用方法：二进制数编码、实数编码、二进制符合编码

### 遗传算子的选择
1. 从种群中选择个体进行遗传操作
2. 常用方法：适应度比例方法、最佳个体保存方法、排序选择方法
#### 选择算子
1. 轮盘选择(FPS)，选择一个个体的概率与其适应度值直接成正比
2. 随机遍历抽样(SUS),但使用多个选择点，只旋转一次转盘就可以同时选择所有个体,这种选择方法可以防止个体被过分反复选择，从而避免了具有特别高适应度的个体垄断下一代
3. 排序选择(Rank-base selection)，排序选择方法类似于轮盘选择，但不是直接使用适应度值来计算选择每个个体的概率，而是将适应度用于对个体进行排序。排序后，将为每个人指定代表其位置的等级，并根据这些等级计算轮盘概率。
4. 适应度缩放选择(Fitness scaling)，适应度缩放将缩放转换应用于原始适应度，将原始适应度值映射到所需范围[a,b], 转换公式：scaledfitness=a×(rawfitness)+b
5. 锦标赛选择(Tournament selection)，从总体中随机选择两个或多个个体，其中适应度得分最高的获胜并被选中，这种选择方法的优势在于，只要可以比较任意两个个体并确定其中哪个更好，就不需要适应度函数的实际值


### 遗传算子交叉
1. 两条染色体部分基因交换，用于结合双亲的遗传信息，以产生（通常是两个）后代
2. 常用方法：（二进制表示的染色体）两点交叉、单点交叉；（实数表示的染色体）算术交叉
#### 交叉算子
1. 单点交叉：在单点交叉法中，随机选择双亲染色体上的位置，该点右边的基因在双亲染色体之间交换，得到了两个后代，每个后代都携带着双亲的一些遗传信息。
2. K点交叉：k点交叉是单点交叉的扩展，在交叉过程中使用k个交叉点，其中k表示正整数
3. 均匀交叉：在均匀交换中，每个基因是通过随机选择一个亲本独立确定的
##### 用于有序列表的交叉
* 考虑到在某些任务中，基于整数的染色体可能代表有序列表的索引。例如在旅行商问题中——假设有几个城市，我们知道每个城市之间的距离，并且需要找到穿过所有城市的最短路线。
1. 有序交叉：（1）随机切割点的两点交叉；（2）从第二个切割点之后开始，按原始顺序遍历所有父母的基因，开始填充每个后代中的其余基因


### 遗传算子的变异
1. 变异是子代基因按小概率扰动产生的变化、增加解的探索范围
2. 常用方法：（二进制）基因变异、依适应度大小变异；(实数表示）按概率
#### 变异算子
1. 位翻转突变：将位翻转突变应用于二进制染色体时，随机选择一个基因，其值被翻转
2. 交换突变：将交换突变应用于基于二进制或整数的染色体时，将随机选择两个基因并交换其值
3. 反转突变：将反转突变应用于基于二进制或整数的染色体时，将选择一个随机的基因序列，并且该序列中的基因顺序颠倒
4. 倒换突变：适用于有序列表的染色体的另一种变异算子是倒换变异，应用后，将选择一个随机基因序列，并将该序列中的基因顺序打乱（或倒换）

### 用于实数编码染色体的遗传算子
* 解空间连续，个体由实数（浮点数）组成
1. 混合交叉(blend crossover)，在混合交叉中，每个后代都是从其父代创建的以下区间中随机选择的：[parent1 − α(parent2 − parent1), parent2 + α(parent2 − parent1)]
2. 模拟二进制交叉(SBX)，背后的想法是模仿二进制编码染色体通常使用的单点交叉的特性。其中特性之一是双亲平均值等于后代的平均值。应用SBX时，两个后代是使用以下公式从双亲创建的：offspring1 = 1/2[(1 + β)parent1 + (1 - β)parent2]; offspring2 = 1/2[(1-β)parent1 + (1+β)parent2]
2.1 其中β是被称为扩展因子的随机数。该公式具有以下显着特性：(1)不管β的值如何，两个后代的平均值等于父母的平均值。(2)当β值为1时，后代是双亲的副本。(3)当β值小于1时，后代间的距离比亲代间的距离更短。(4)当β值大于1时，后代间的距离比双亲间的距离更远。
3. 实数突变，(1)生成一个位于原始个体附近的随机实数，（2）随机产生的新值代替原有实数值

### 适应度函数
1. 即由优化问题的目标函数生成的评价函数

### 4个运行参数常用值为：
1. 群体大小M：20-100
2. 进化代数T：100-500
3. 交叉概率Pc：0.4-0.99
4. 变异概率Pm：0.0001-0.1
