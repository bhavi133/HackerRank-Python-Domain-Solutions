Link : https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

nums = list(map(int, input().split()))
arr = numpy.array(nums)
print(numpy.reshape(arr, (3, 3)))
