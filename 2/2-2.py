def isleap (s):
    if s % 400 == 0:
        return True
    elif s % 4 == 0 and s % 100 != 0 :
        return True
    else :
        return False
print(isleap(int(input())))