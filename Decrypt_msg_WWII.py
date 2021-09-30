"""
Question:
f(N+1)=(f(N) XOR (f(N)+1)) mod 1000 where f(0)=0

For instance, lets assume that N is 4, so you are trying to find f(4):
f(0)=0
f(1)=(0 XOR 1) mod 1000=1
f(2)=(1 XOR 2) mod 1000=3
f(3)=(3 XOR 4) mod 1000=7
f(4)=(7 XOR 8) mod 1000=15

Your duty is to find the header positions of M given messages by using N provided for each of them. Remember, Germans might change their algorithms overnight, your time is short and valuable (End of Transmission)

Britain shall prevail!

Hint: Think in cycles, maybe there's a way to predict the future
"""

"""
Question:
f(N+1)=(f(N) XOR (f(N)+1)) mod 1000 where f(0)=0

For instance, lets assume that N is 4, so you are trying to find f(4):
f(0)=0
f(1)=(0 XOR 1) mod 1000=1
f(2)=(1 XOR 2) mod 1000=3
f(3)=(3 XOR 4) mod 1000=7
f(4)=(7 XOR 8) mod 1000=15

Your duty is to find the header positions of M given messages by using N provided for each of them. Remember, Germans might change their algorithms overnight, your time is short and valuable (End of Transmission)

Britain shall prevail!

Hint: Think in cycles, maybe there's a way to predict the future
"""


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def f(num):
    if num == 1:
        return 1
    else:
        return (f(num-1)^(f(num)))%1000



m = int(input())
for i in range(m):
    sum = 0
    n = int(input())
    for i in range(n):
         sum = sum*2 + 1
       
    print(sum)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

