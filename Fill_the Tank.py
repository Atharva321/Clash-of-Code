"""
You need to calculate if it is possible to fuel up a spaceship within the number of seconds allowed(t), given the capacity of the tank (c) in litres, and the number of litres of fuel that can be pumped into its tank per second (r).

The tank starts empty.
The maximum amount of litres per second (r) is constantly pumped into the tank until it is full.
Input
Line 1: Three space seperated integers t, c, and r.
Output
Line 1: An string "yes" or "no". "yes" if it is possible to fill up the spaceship in the time allowed, "no" if it is not possible.
Constraints
0 < t ≤ 10,000
0 < c ≤ 10,000
0 < r ≤ 1000


# """
# Time  : O(1)
# Space : O(1)

t, c, r = [int(i) for i in input().split()]
print("yes" if c<=r*t else "no")
