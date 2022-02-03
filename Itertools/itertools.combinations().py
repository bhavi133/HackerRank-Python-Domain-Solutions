Link : https://www.hackerrank.com/challenges/itertools-combinations/problem

import itertools

str1, k = list(map(str, input().split(' ')))
k = int(k) + 1
str2 = sorted(str1)
for i in range(1, k):
    for j in list(itertools.combinations(str2, i)):
        print(''.join(j))
