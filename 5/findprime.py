def be (x) :
    num = []
    time = []
    now = 2    
    while  x != 1:
        count = 0
        while x % now == 0 :
            count += 1
            x /= now
        if count > 0 :
            num.append(now)
            time.append(count)
        now += 1
    return num , time
def Main() :
    n=int(input())
    num , time = be(n)
    print(num)
    print(time)
Main()