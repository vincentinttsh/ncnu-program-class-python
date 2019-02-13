import sys
def cycleLength (seed) :
    times = 1 #times
    while seed != 1 : 
        times += 1
        if seed % 2 == 1 : #odd
            seed = 3*seed+1
        else : #even
            seed = seed/2 
    return times
for data in sys.stdin: #input
    if data =='\n' : #no input ,just enter
        break;
    first,second = map(int,data.split()) #separate and change to int 
    maxa = 0 #biggest
    for seed in range(min(first,second),max(first,second)+1): #small to big
        maxa = max(maxa,cycleLength(seed))  #maxa will have the biggest number
    print (first,second,maxa)