import sys , math
def prime (x) :
    num = int(x)
    now = 2 #從2開始找是否有除了1與自己以外的因數
    while now < int(math.sqrt(num))+1 : #找到根號就行了
        if(num % now == 0) : #找到一個就結束
            return False
        now+=1
    return True
count = 0
num = int(input())
for i in range(2,num+1) : #1一定不是，故從2到num
    if prime(i):
        count+=1
print(count)