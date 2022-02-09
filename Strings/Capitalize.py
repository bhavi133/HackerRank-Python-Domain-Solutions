Link  : https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

def solve(s):
    str1 = s.split(' ')
    list1 = [i.capitalize() for i in str1]
    return " ".join(list1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
