Link : https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np

n = int(input())
np.set_printoptions(legacy='1.13')
array = np.array([input().split() for i in range(n)], float)
print(np.linalg.det(array))
