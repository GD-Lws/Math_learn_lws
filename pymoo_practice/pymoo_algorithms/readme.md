# List Of Algorithms
* Algorithms available in pymoo¶
| Algorithm | Class | Objective(s) | Constraints | Description |
| :--: | :--: | :--: | :--: | :--: |
| Genetic Algorithm | GA | single | x | A modular implementation of a genetic algorithm. It can be easily customized with different evolutionary operators and applies to a broad category of problems. |
| Differential Evolution | DE | single | x | Different variants of differential evolution which is a well-known concept for in continuous optimization especially for global optimization. |

Biased Random Key Genetic Algorithm

BRKGA

single

x

Mostly used for combinatorial optimization where instead of custom evolutionary operators the complexity is put into an advanced variable encoding.

Nelder Mead

NelderMead

single

x

A point-by-point based algorithm which keeps track of a simplex with is either extended reflected or shrunk.

Pattern Search

PatternSearch

single

x

Iterative approach where the search direction is estimated by forming a specific exploration pattern around the current best solution.

CMAES

CMAES

single

Well-known model-based algorithm sampling from a dynamically updated normal distribution in each iteration.

Evolutionary Strategy

ES

single

The evolutionary strategy algorithm proposed for real-valued optimization problems.

Stochastic Ranking Evolutionary Strategy

SRES

single

x

An evolutionary strategy with constrained handling using stochastic ranking.

Improved Stochastic Ranking Evolutionary Strategy

ISRES

single

x

An improved version of SRES being able to deal dependent variables efficiently.

NSGA-II

NSGA2

multi

x

Well-known multi-objective optimization algorithm based on non-dominated sorting and crowding.

R-NSGA-II

RNSGA2

multi

x

An extension of NSGA-II where reference/aspiration points can be provided by the user.

NSGA-III

NSGA3

many

x

An improvement of NSGA-II developed for multi-objective optimization problems with more than two objectives.

U-NSGA-III

UNSGA3

many

x

A generalization of NSGA-III to be more efficient for single and bi-objective optimization problems.

R-NSGA-III

RNSGA3

many

x

Allows defining aspiration points for NSGA-III to incorporate the user’s preference.

MOEAD

MOEAD

many

Another well-known multi-objective optimization algorithm based on decomposition.

AGE-MOEA

AGEMOEA

many

Similar to NSGA-II but estimates the shape of the Pareto-front to compute a score replacing the crowding distance.

C-TAEA

CTAEA

many

x

An algorithm with a more sophisticated constraint-handling for many-objective optimization algoritms.

SMS-EMOA

CTAEA

many

x

An algorithm that uses hypervolume during the environmental survival.

RVEA

RVEA

many

x

A reference direction based algorithm used an angle-penalized metric.