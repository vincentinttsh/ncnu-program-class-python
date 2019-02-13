import cmath
import math
def findroots (a,b,c):
    if a != 0 :
        if b*b-4.0*a*c < 0:
            d=(-b+cmath.sqrt(b*b-4*a*c))/(2*a)
            e=(-b-cmath.sqrt(b*b-4*a*c))/(2*a)
        else :
            d=(-b+math.sqrt(b*b-4*a*c))/(2*a)
            e=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return d,e
    elif b!= 0 :
        return -c/b
    elif c!= 0 :
        return []
    else :
        return "infinite"
a = float(input())
b = float(input())
c = float(input())
roots = findroots(a,b,c)
print(roots)
