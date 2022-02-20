Link : 

import numpy

n, m = map(int,input().split())
a = []
for i in range(n):
    row = list(map(int,input().split()))
    a.append(row)

arr = numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())
