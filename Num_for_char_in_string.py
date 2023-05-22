

import sys
import math


s = input().split(" ")
e=""
for i in s:
    a=list(i)
    b=[x.upper() for x in a if str(x).isalpha()]
    b=list(set(b))
    b=sorted(b,key=ord)
    
    for w in i:
        if w.upper() in b:
            e+=str(b.index(w.upper())+1)
        else:
            e+=w
    e+=" "
print(e[:-1])
