import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width = int(input())
height = int(input())
corner = input()
vertical_sides = input()
horizontal_sides = input()
composition = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(0,width):
    for j in range(0,height):
        if((i == 0 and j ==0) or (i==0 and j==width-1)or(i==height-1 and j==0)or(i==width-1 and j==height-1)):
            print(corner,end="")
        elif(i==0 or i==height-1):
            print(horizontal_sides,end="")
            
    print()
"""
for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (i == 0 || i == height - 1) {
                if (j == 0 || j == width -1) {
                    cout << corner;
                } else {
                    cout << horizontalSides;
                } 
            } else {
                if (i > 0 && i < height - 1 && (j == 0 || j == width - 1)) {
                    cout << verticalSides;
                } else {
                    cout << composition;
                }
                
            }
            
        }
        cout << endl;
    }
"""
