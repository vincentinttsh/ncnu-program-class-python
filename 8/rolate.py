def printa (squre) :
    for i in range(len(squre)) :
        for j in range(len(squre[i])) :
            print(squre[i][j],end=' ')
        print()
R,C,M = map(int,input().split())
squre = list()
for i in range(R) :
    squre.append(list(map(int,input().split())))
for cmd in map(int,input().split()) :
    if cmd == 1  :
            squre = [squre[R-x-1] for x in range(R)]
    else :
        temp = list()
        for y in range (C) :
            temp.append(list())
            for z in range (R-1,-1,-1) :
                temp[y].append(squre[z][y])
        squre , C , R = temp , R , C    
print(R,C)
printa(squre) 
