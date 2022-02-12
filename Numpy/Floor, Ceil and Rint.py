Link :  https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np

arr = np.array(input().split(), float)
np.set_printoptions(legacy='1.13')
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
