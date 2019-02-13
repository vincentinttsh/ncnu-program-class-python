def canhu ( cards , n , needmj ) :
    if n == 0 :
        return True
    if needmj == True : # have no pair 
        for i in range (34) :
            if cards[i] >= 2 :#check 2 same
                cards[i] -= 2
                if canhu(cards , n-2 , False) :
                    return True
                cards[i] += 2
    for i in range (34) : 
        if cards[i] >= 3 :#check 3 same
            cards[i] -= 3
            if canhu(cards , n-3 , needmj) :
                    return True
            cards[i] += 3
        if i < 27 and i % 9 < 7 and cards[i] > 0 and cards[i+1] > 0 and cards[i+2] > 0 : #check continuity
            cards[i] , cards[i+1] , cards[i+2] = cards[i]-1 , cards[i+1]-1 , cards[i+2]-1 
            if canhu(cards , n-3 , needmj) :
                    return True
            cards[i] , cards[i+1] , cards[i+2] = cards[i]+1 , cards[i+1]+1 , cards[i+2]+1 
    return False # impossible
def main() :
    have = list(map(int , input().split()))
    chinese = ('一','二','三','四','五','六','七','八','九','萬','筒','條','東','南','西','北','中','發','白')
    total , i  = 1 , 0
    for x in have :
        total += x
    while i < 34:
        have[i] = have[i] + 1
        if canhu(have[:] , total , True) == True :
            if i < 27 :
                print(chinese[i%9]+chinese[9+i//9],end=' ') # number+color
            else :
                print(chinese[i-15],end=' ') # word
        have[i] = have[i] - 1
        i += 1
    print()
main()
