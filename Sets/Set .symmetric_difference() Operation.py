Link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

e = int(input())
e = set(map(int, input().split()))
f = int(input())
f = set(map(int, input().split()))
print(len(e.symmetric_difference(f)))
