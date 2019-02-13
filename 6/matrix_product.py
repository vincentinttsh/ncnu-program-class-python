A , B = list() ,list()
i,j=map(int,input().split())
for p in range(0,i) :
    A.append(list(map(int,input().split())))
q,w=map(int,input().split())
for p in range(0,q) :
    B.append(list(map(int,input().split())))
c = [[0 for x in range(0,w)]for y in range(0,i)]
for m in range(0,i):
    for a in range(0,q):
        for s in range(0,w):
            c[m][s]+=A[m][a]*B[a][s]
for now in range(0,i):
    for noww in range(0,w):
        print('\t'+c[now][noww],end=' ')
    print()