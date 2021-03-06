"""

You have a garden of C tomato crops, and you want to cook an amazing soup of N tomatoes in D days. Each tomato crop is represented by a digit from 0 to 9, which is how many days you have to wait until harvest it.

Example: If your garden is 2224, you'll harvest 3 tomatoes in 2 days, and 1 tomato in 4 days.

Goal: In D days, will you be able to cook a beautiful soup containing at least N tomatoes from your garden?
Input
Line 1: Tomato crops C, Needed tomatoes for the soup N, Delay until soup-day D
Line 2: Garden, C digits from 0 to 9 representing how many days you have to wait to harvest each crop
Output
"YOU_CAN_MAKE_A_SOUP_IN_D_DAYS" if you have enough tomatoes after D days to make a soup, or "YOU_CANNOT_MAKE_A_SOUP_IN_D_DAYS".
Constraints
0 < C < 1000
0 ≤ N < 1000
0 ≤ D < 10
Example
Input

20 10 5
44444444444444444444

Output

YOU_CAN_MAKE_A_SOUP_IN_5_DAYS

"""

I=input
c,t,d=[int(i)for i in I().split()]
S=''
if sum(1for c in I()if int(c)<=d)<t:S='NOT'
I(f'YOU_CAN{S}_MAKE_A_SOUP_IN_{d}_DAYS')

"""
My Code:
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

crops, tomatoes, delay = [int(i) for i in input().split()]
g = input()
garden = [len(g)]
for j in range(0,len(g)):
    garden[j] = int(g[j])
sort(garden)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
D=0
for i in range(0,crops):
    if(garden[i]<=delay):
        D = D +1
if(D<=tomatoes):
    print("YOU_CAN_MAKE_A_SOUP_IN_"+str(dalay)+"_DAYS")    
else:
    print("YOU_CAN(NOT)_MAKE_A_SOUP_IN_"+str(delay)+"_DAYS")

"""
