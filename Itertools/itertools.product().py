Link : https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list((product(list1, list2)))
for i in list3:
    print(i, end=" ")
