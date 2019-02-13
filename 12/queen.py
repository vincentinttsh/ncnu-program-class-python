def queen( n , row , ans , col , us , ds ): # us = slash  ds = back slash
    if n == row :
        printt(ans)
        print('-------------------------')
        return
    for c in range(n) : #check each colum
        if col[c] and us [row+c] and ds[row-c+n-1] :
            ans[row][c] , col[c] , us[row+c] , ds[row-c+n-1] = 1 , False , False , False
            queen(n,row+1,ans,col,us,ds)
            ans[row][c] , col[c] , us[row+c] , ds[row-c+n-1] = 0 , True , True , True
def printt(ls) :
    for i in range(len(ls)) :
        for j in range(len(ls[i])) :
            print(ls[i][j],end=' ')
        print()
def Main():
    n = int(input())
    queen(n,0,[[0 for y in range(n)]for x in range(n)],
        [True for i in range(n)],[True for i in range(2*n-1)],[True for i in range(2*n-1)])
Main()