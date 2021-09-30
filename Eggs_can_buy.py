import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())

print(n if n<m else m)

"""
My Solution:
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if(n==0 or m==0):
    print("0")

elif(n<m):
    print(str(m-n))

else:
    print(str(m))
"""
