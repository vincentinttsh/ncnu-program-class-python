def find (data , pos , size , ans ) :
    if len(ans) == size :
        print(ans)
        return
    for x in range(pos , len(data)):
        ans.append(data[x])
        find(data , x+1 , size , ans)
        ans.remove(data[x])
def Main() :
    have = list(map(int,input().split()))
    num = [i for i in range(1,50)]
    for x in have :
        num.remove(x)
    find (num , 0 , 6 , have)
Main()