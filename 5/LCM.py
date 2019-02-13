from math import sqrt
def be (x) : #質因數分解
    num = []
    time = []
    now = 2    
    while  x != 1 :
        count = 0
        while x % now == 0 : #成立時now必為質數
            count += 1
            x //= now
        if count > 0 : #代表他有此質因數
            num.append(now)
            time.append(count)
        now += 1 
    return num , time
def findlcm (i,j) :
    result =dict()
    for i in range(i,j+1) : 
        base , exp = be(i) #取的該數質因數分解
        now = 0
        while now < len(base) :
            if base[now] in result: #有此數就取的次方最大
                result[base[now]]= max(result[base[now]],exp[now])
            else : #沒有就加入dict
                result[base[now]]= exp[now]
            now+=1
    return result
def Main():
    n=input()
    a,b= map(int,n.split())
    result = findlcm(a,b)
    d=1
    for i in result.keys():
        d *=i**result[i]
    print(d)
Main()