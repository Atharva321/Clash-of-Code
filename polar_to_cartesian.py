import sys
import math as m
i,p=input,round
f,r=map(float,[i(),i()])
k=2*m.pi/360
print(f'{p(r*m.cos(f*k),1)}, {p(r*m.sin(f*k),1)}')
