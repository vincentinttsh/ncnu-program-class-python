def erase (n) : # 製作質數表
    data = list()
    num = [True for i in range(n+1)]    
    for i in range (2,n+1) :
        if num[i] == True :
            m = 2
            data.append(i)
            while m * i <= n : # 刪除其倍數
                num[m * i] , m = False , m + 1
    return data
def find (n,data,pos,ans):
    if n < 0 : # 非解
        return False
    if n == 0 : #為解
        print(ans)
        return True
    for x in range(pos,-1,-1) :
        ans.append(data[x]) # 加入一個可能的質數
        if find(n-data[x],data,x-1,ans) :
            return True
        ans.remove(data[x]) #因為不可能有此質數，故刪除
    return False
def Main() :
    ask = int(input())
    data = erase(ask)
    find(ask,data,len(data)-1,[])
Main()