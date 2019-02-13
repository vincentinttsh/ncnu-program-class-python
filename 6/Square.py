def Make_Squre(n): #
    y , x = 0 , n//2 # 啟始點
    ans = [[0 for a in range(n)]for b in range(n)]
    for now in range(1,n*n+1) :
        ans[y][x] , y , x = now , y-1 , x+1 #依序輸入
        if y == -1 and x != n : #在上面超出 and not 特殊點的特殊規則 
            y = n - 1 
        elif x == n and y != -1 : #在右邊超出 and not 特殊點的特殊規則
            x = 0
        elif (x == n and y == -1) or (ans[y][x]>0): #特殊點的特殊規則 or 該點已有數字
            x , y = x-1 , y+2
    return ans
def print_all (thing,n) :
    for a in range(n) :
        for b in range(n) :
            print('{0:3d}'.format(thing[a][b]),end=' ')
        print()
def Main():
    n = int(input())
    print_all(Make_Squre(n),n)
Main()