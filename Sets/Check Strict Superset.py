Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(input().split())
n = int(input())
flag = True
for i in range(n):
    s = set(input().split())
    if (s & a != s) or (s == a):
        flag = False
        break
print(flag) 
