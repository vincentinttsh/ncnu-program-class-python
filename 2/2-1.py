def isleap (s):
    if s % 400 == 0:
        return True
    else :
        if s % 100 == 0 :
            return False
        else :
            if s % 4 ==0 :
                return True
            else :
                return False
print(isleap(int(input())))