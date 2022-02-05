#My Solution

c,j=input(),0
while(j<6):
 print(int(c[j+1:j+3],16))
 j+=2

"""
converting the RGB tod decimal.
for single sentence we cna write the body statement 
after the loop syntax
Shortest Solution
c=input()
for i in range(1,7,2):print(int(c[i:i+2],16))
"""
