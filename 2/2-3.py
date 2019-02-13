import sys
def isleap (s):
    if s % 400 == 0:
        return True
    elif s % 4 == 0 and s % 100 != 0 :
        return True
    return False
for s in sys.stdin:
    print(isleap(int(s)))