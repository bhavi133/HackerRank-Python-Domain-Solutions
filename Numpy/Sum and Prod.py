Link : https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

arr = np.array(a)
print(np.product(np.sum(arr, axis=0)))
