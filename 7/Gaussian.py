def ans(n) :
    squre=list()
    for i in range(n) :
        squre.append(list(map(float,input().split())))
    for x in range(0,n-1) : #由上往下消    
        for y in range(x+1,n) : #被消的列
            if squre[x][x] == 0 :
                k = x+1
                while k < n and squre[k][x] :
                    k+=1
                if k == n :
                    print("error")
                    return
                squre[k] , squre[x]= squre[x] , squre[k]
            t = squre[y][x] / squre[x][x] #乘數
            for z in range(0,n+1) : #被消的格子
                squre[y][z] -= squre[x][z] * t
    for x in range(n-1 , 0 , -1) : #由下往上消
        for y in range(x-1 , -1 , -1) : #被消的列
            if squre[x][x] == 0 :
                k = x-1
                while k >=0 and squre[k][x] :
                    k-=1
                if k == -1 :
                    print("error")
                    return
                squre[k] , squre[x]= squre[x] , squre[k]
            t = squre[y][x] / squre[x][x] #乘數
            for z in range( 0 , n+1 , 1) : #被消的格子
                squre[y][z] -= squre[x][z] * t
    for x in range (n) : #前面調整為1
        squre[x][n] /= squre[x][x]
        squre[x][x] /= squre[x][x]
    for i in range(n) :
        print(squre[i][n])
def Main() :
    ans(int(input()))
Main()
