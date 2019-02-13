m =int(input())
n = 1
while n <= m:
    print (' '*(m-n),end='')
    print('*'*(2*n-1))
    n+=1
n-=2
while n >= 1 :
    print (' '*(m-n),end='')
    print('*'*(2*n-1))
    n-=1