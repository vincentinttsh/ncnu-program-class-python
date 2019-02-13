def step (n , tar_1 , tar_2 , tar_3) :
    if n == 1 :
        return [(tar_1 , tar_3)]
    else :
        return step(n-1 , tar_1 , tar_3 , tar_2)+step(1 , tar_1 , tar_2 , tar_3)+step(n-1 , tar_2 , tar_1 , tar_3)
for move in step(int(input()) , 'A' , 'B' , 'C') :
    print('place move %c to %c' % move)