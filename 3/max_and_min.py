a = int(input("how many number?"))
now = 2
temp = int(input())
maxa=mina=temp
while now <= a :
    temp = int(input())
    maxa = max(temp,maxa)
    mina = min(temp,mina)
    #if maxa < temp :
    #	maxa = temp
    #if mina > temp :
    #	mina = temp
    now = now + 1
print ("max : ",maxa,"min : ",mina)