#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n):
    while len(str(n))!=3:
        n = list(str(sum(n)))
        n = [int(x) for x in n]
        superDigit(n)
    return n[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])
    arg = list(str(n)*k)
    arg = [int(x) for x in arg]
    result = superDigit(arg)

    fptr.write(str(result) + '\n')

    fptr.close()
