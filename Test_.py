import numpy as np

c1 = np.arange(0, 5)
print(c1)
d = np.array([3, 4, 1, 0, 2])
print(d)
c1[d] = np.array([0, 1, 2, 3, 4])
print(c1)
c1[d] = np.arange(0, 5)
print(c1)
