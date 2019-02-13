def build (n) :
    if n <= 1 :
        return n
    return build(n-1) + build(n-2)
print(build(int(input())))