Link : https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

arr = np.array(a)
print(np.max(np.min(arr, axis=1)))
