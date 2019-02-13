n = int(input())
squre = list()
squre.append(list())
squre.append(list())
squre[1].append(1)
for i in range(2,n+1) :
    squre.append(list(squre[i-1]))
    for j in range(1,i-1) :
        squre[i][j] += squre[i-1][j-1]
    squre[i].append(1)
for i in range(1,n+1) :
    for j in range(0,i) :
        print('{0:5d}'.format(squre[i][j]),end = '')
    print()