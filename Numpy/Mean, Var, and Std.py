Link : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

arr = np.array(a)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr, axis=None), 11))
