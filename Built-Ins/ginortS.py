Link : https://www.hackerrank.com/challenges/ginorts/problem

str1 = input()
str1 = sorted(str1, key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x))
print("".join(str1))
