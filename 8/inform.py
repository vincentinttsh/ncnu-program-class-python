def find (elem , thing , no) : #尋找目標
    for x in range(len(elem)) :
        if int(elem[x][no]) == int(thing) :
            return x
def main() :
    peo = list() # 欠錢的人
    for i in range(int(input())) :
        peo.append(input().split())
    for i in range(int(input())) : # 欠錢的人的配偶
        temp = input().split()
        peo[find(peo,temp[0],0)].append(temp[2])
        peo[find(peo,temp[2],0)].append(temp[0])
    peo.sort(key=lambda x:int(x[2]), reverse = True) #依錢由大到小
    for i in range(200) :
        if len(peo[i]) == 4 : # 不是單身狗
            x = find(peo,peo[i][3],0) # 尋找配偶
            if int(peo[x][2]) > 500000 : # 配偶夠有錢
                print('{0:8} {1:3}'.format(peo[x][0],peo[x][1]))
main()