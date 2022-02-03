Link : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

import itertools

str1, k = list(map(str, input().split(' ')))
str2 = sorted(str1)
for i in list(itertools.combinations_with_replacement(str2, int(k))):
    print(''.join(i))
