Link : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy

n = list(map(int, input().split()))
N = tuple(n)
print(numpy.zeros(N, numpy.int))
print(numpy.ones(N, dtype=numpy.int))
