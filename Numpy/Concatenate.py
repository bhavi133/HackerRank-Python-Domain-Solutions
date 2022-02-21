Link : https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

n, m, p = map(int, input().split())
a1 = []
a2 = []
for i in range(n):
    row = list(map(int, input().split()))
    a1.append(row)

for i in range(m):
    row = list(map(int, input().split()))
    a2.append(row)

arr1 = np.array(a1)
arr2 = np.array(a2)
print(np.concatenate((arr1, arr2), axis=0))
