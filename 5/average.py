import math
def cal(data , n) :
    total = 0.0
    for i in data :
        total += i
    total /= n
    g = 0.0
    for i in data :
        g += (i-total) * (i-total)
    return total , math.sqrt(g/n)
def Main() :
    n = int(input())
    now = 1
    score=[]
    while now <= n :
        score.append(float(input()))
        now += 1
    print(cal(score,n))
Main()