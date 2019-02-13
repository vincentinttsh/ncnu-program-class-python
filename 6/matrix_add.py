n = input()
i,j=map(int,n.split())
A=list()
B=list()
now = 0
while now < i :
    n=input()
    A.append(list(map(int,n.split())))
    now += 1
now = 0
while now < i :
    n=input()
    B.append(list(map(int,n.split())))
    now += 1
m = n = 0
C=A
while m < i :
    n = 0
    while n < j :
        print('{3d:0}'.format(A[m][n] + B[m][n]),end = ' ')
        n += 1
    print()
    m += 1