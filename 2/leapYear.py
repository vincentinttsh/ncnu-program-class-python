# 判別閏年
def isleap (s): 
    if s % 400 == 0:
        return True
    elif s % 4 == 0 and s % 100 != 0 :
        return True
    else :
        return False
if isleap(int(input("Please input a year: "))) :
    print("加薪!!")
else :
    print("沒有加薪QQ")