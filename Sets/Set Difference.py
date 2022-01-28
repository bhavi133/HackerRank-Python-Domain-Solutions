Link : https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
M = set(map(int, input().split()))
N = int(input())
N = set(map(int, input().split()))
set1 = M.difference(N)
set2 = N.difference(M)
for i in sorted(set1.union(set2)):
    print(i)
