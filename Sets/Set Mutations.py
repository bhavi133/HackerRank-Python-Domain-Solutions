Link : https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
a = set(map(int, input().split()))
N = int(input())
for i in range(N):
    res = input().split()
    option = res[0]
    s = set(map(int, input().split()))
    if (option == 'update'):
        a |= s
    elif (option == 'intersection_update'):
        a &= s
    elif (option == 'difference_update'):
        a -= s
    elif (option == 'symmetric_difference_update'):
        a ^= s
print(sum(a))
