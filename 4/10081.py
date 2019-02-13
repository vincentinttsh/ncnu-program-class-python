n = int(input())
def reverse (num) :
    data = str(num)
    done = ''
    now = 0
    while now < len(data) :
        done += data[len(data)-1-now]
        now+=1
    return done
while n > 0 :
    data = str(input())
    count = 0
    while data != reverse(data) :
        count+=1
        data = str(int(data)+int(reverse(data)))
    print(count,data)
    n-=1