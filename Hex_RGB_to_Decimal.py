#My Solution

c,j=input(),0
while(j<6):
 print(int(c[j+1:j+3],16))
 j+=2

"""
  
Shortest Solution

c=input()
for i in range(1,7,2):print(int(c[i:i+2],16))

"""
