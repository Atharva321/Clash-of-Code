import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
percentage = int(input())
bill_t = 0
tip_t = 0
for i in range(n):
    bill, tip = [float(j) for j in input().split()]
    bill_t += bill
    tip_t += tip

if tip_t/bill_t*100>=percentage:
    print("DRUNK")
else:
    print("THIRSTY")


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


