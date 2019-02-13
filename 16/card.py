import random
def Main() :
    player = ['N','E','S','W'] #玩家
    card = [[],[],[],[]] #每個玩家的牌
    color = ['S','H','D','C'] #花色
    number = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #數字
    have = [False for x in range(52)] #有無有人有此牌
    for i in range (52):
        x = random.randint(0,51) #隨機一張
        while have[x] : #已給過 ， 再隨機一張
            x = random.randint(0,51)
        card[i%4].append(x) #給玩家
        have[x] = True #紀錄已給過
    for i in range(len(card)):
        print('['+player[i]+']:',end='') # 輸出玩家
        card[i].sort() #把牌排好
        now = -1 #花色
        for x in card[i]:
            if x < now*13+13: #在此花色下
                print(number[x%13],end=' ')
            else : #換花色
                now = x//13
                print()
                print(color[now]+' - '+number[x%13],end=' ')
        print()
Main()