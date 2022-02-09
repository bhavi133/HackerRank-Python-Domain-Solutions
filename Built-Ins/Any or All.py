Link : https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
lst = list(map(int, input().split(" ")))
arr = sorted(lst)
if(arr[0] <= 0):
    print(False)
else:
    flag = False
    for i in arr:
        s = str(i)
        if (s == s[::-1]):
            flag = True
            break
    print(flag)
