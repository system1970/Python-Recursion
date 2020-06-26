#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n):
    while len(str(n)) != 1:
        n = sum([int(x) for x in str(n)])
        print(n)
        superDigit(n)
    return n

n,k = list(map(int,input().split()))
n = [int(x) for x in str(n)]
# n = nk[0]

# k = int(nk[1])
# arg = list(str(n)*k)
# arg = [int(x) for x in arg]
# result = superDigit(arg)
print(superDigit(sum(n)*k))
