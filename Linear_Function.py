Time  : O(n)
Space : O(1)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    x = int(input())
    print(a*x+b)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

