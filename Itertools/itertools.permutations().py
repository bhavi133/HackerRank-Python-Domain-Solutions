Link : https://www.hackerrank.com/challenges/itertools-permutations/problem

import itertools

str1, k = list(map(str, input().split(' ')))
str2 = sorted(str1)
for i in list(itertools.permutations(str2, int(k))):
    print(''.join(i))
