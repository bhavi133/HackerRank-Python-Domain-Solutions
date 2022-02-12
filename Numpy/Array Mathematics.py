Link : https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy

n, m = map(int,input().split())
arr1 = []
arr2 = []
for i in range(n):
    tmp = list(map(int,input().split()))
    arr1.append(tmp)
for i in range(n):
    tmp = list(map(int,input().split()))
    arr2.append(tmp)
    
np_arr1 = numpy.array(arr1)
np_arr2 = numpy.array(arr2)
print(np_arr1 + np_arr2)
print(np_arr1 - np_arr2)
print(np_arr1 * np_arr2)
print(np_arr1 // np_arr2)
print(np_arr1 % np_arr2)
print(np_arr1 ** np_arr2)
