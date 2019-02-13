allnum = []
from math import sqrt
def findPrime (x) : #質因數分解
    result = dict()
    if x == 1 :
        result[1] = 1
        allnum.append(result)
        return result
    now = min(len(allnum)-1,int(sqrt(x))+1)
    while now >= 1 and x != 1:
        if x % (now+1) == 0 :
            for i in allnum[now].keys() :
                if i in result :
                    result[i]+=allnum[now][i]
                else :
                    result[i]=allnum[now][i]
            x = x // (now+1)
        else :
            now = min(now-1,int(sqrt(x))+1)
    if x != 1 :
        result[x] = 1
    allnum.append(result)
    return result 
def findlcm (s , e) :
    ans =dict()
    while s <= e:
        for i in allnum[s-1].keys():
            if i in ans :
                ans[i] = max(ans[i],allnum[s-1][i])
            else :
                ans[i] = allnum[s-1][i]
        s+=1
    return ans
def Main():
    n=input()
    a,b= map(int,n.split())
    start =1
    while start <= b:
        findPrime(start)
        start+=1
    result = findlcm(a,b)
    ans=1
    for i in result.keys():
        ans *=i**result[i]
    print(ans)
Main()
