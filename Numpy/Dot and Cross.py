Link : https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

n = int(input())
a = []
b = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)
    
arr1 = np.array(a)
arr2 = np.array(b)
print(np.dot(arr1, arr2))
