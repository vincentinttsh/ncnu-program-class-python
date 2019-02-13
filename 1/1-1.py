import cmath
import math
a = float(input())
b = float(input())
c = float(input())
if b*b-4.0*a*c < 0:
    d=(-b+cmath.sqrt(b*b-4*a*c))/(2*a)
    e=(-b-cmath.sqrt(b*b-4*a*c))/(2*a)
else :
    d=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    e=(-b-math.sqrt(b*b-4*a*c))/(2*a)
print(d,e)
