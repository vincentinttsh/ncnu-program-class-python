import matplotlib.pyplot as plt
import math
xlist = []
ylist = []
def line (len , x, y , theta) :
    if len <= 1 :
        xlist.append(x)
        ylist.append(y)
        return
    line(len//3,x,y,theta)    
    line(len//3,x+math.cos(theta/180*math.pi)*len/3 , y+math.sin(theta/180*math.pi)*len/3,theta+60)
    line(len//3,x+math.cos((theta+30)/180*math.pi)*len*math.sqrt(3)/3 , y+math.sin((theta+30)/180*math.pi)*len*math.sqrt(3)/3,theta-60)
    line(len//3,x+math.cos(theta/180*math.pi)*len/3*2 ,y+math.sin(theta/180*math.pi)*len/3*2,theta)
def Main():
    x , y = -50 , 0
    plt.xlim(-100,100)
    plt.ylim(-100,100)
    for i in range (3) :
        line(3**4,x,y,240*i)
        x = xlist[len(xlist)-1]
        y = ylist[len(ylist)-1]
    plt.plot(xlist,ylist,markersize=1)
    plt.show()
Main()