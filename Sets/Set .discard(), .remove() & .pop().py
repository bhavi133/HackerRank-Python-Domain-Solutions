Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    res = list(input().split(" "))
    if (len(res) == 1):
        s.pop()
    else:
        value = int(res[1])
        s.discard(value)
print(sum(s))
