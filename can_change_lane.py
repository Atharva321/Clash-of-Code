"""
There is a car in the left lane that needs to merge into the right lane. The car cannot safely change lanes if any of the following are true:

1. There is another car directly to the right that is traveling the same speed
2. There is a car ahead and to the right that is traveling slower
3. There is a car behind and to the right that is traveling faster
Input
Three rows of two-character strings indicating the location and speed of the cars.
| indicates no car is present.
An integer between 1 and 9 inclusive indicates a car traveling at that speed.
Traffic is moving upwards; in other words, the top row indicates the front of the traffic and the bottom row indicates the back of the traffic.

Example:

|3
2|
|1

Output
true if the car can safely change lanes, false otherwise.
Constraints
1 ≤ all speeds ≤ 9
Example
Input

||
1|
||

Output

true

"""
#My incomplete solution

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
flag = "false"
for i in range(3):
    line = input()
    if line[0]== "|" and line[1] == "|":
       flag = "true"
    elif line[0]== "|" or line[1] == "|":
       flag = "true"
    else:
        flag="false"
    if line[0]!= "|" and line[1] == "|":
        previous = int(line[0])
    if line[0]== "|" and line[1] != "|":
        previous = int(line[1])
print(flag) 
