def perm (data , pos , ans):
    if pos == len(data) :
        print(ans)
        return
    for x in range(pos , len(data)):
        ans.append(data[x])
        data[pos] , data[x] = data[x] , data[pos]
        perm(data,pos+1,ans)
        data[pos] , data[x] = data[x] , data[pos]
        ans.remove(data[x])
def com (data , pos , size , ans ):
    if len(ans) == size :
        print(ans)
        return
    for x in range(pos , len(data)):
        ans.append(data[x])
        com(data , x+1 , size , ans)
        ans.remove(data[x])
data = input().split()
perm(data,0,[])
print()
com(data,0,3,[])