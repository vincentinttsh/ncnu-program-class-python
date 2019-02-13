import matplotlib.pyplot as plt
xa = []
ya = []
def fractal(size, x, y):
    if size == 1:
        xa.append(x)
        ya.append(y)
        return
    fractal(size//3, x, y)
    fractal(size//3, x+size//3, y)
    fractal(size//3, x+2*size//3, y)
    fractal(size//3, x, y+size//3)
    fractal(size//3, x+2*size//3, y+size//3)
    fractal(size//3, x, y+2*size//3)
    fractal(size//3, x+size//3, y+2*size//3)
    fractal(size//3, x+2*size//3, y+2*size//3)
def Main():
    plt.figure()
    fractal(81, 100, 100)
    plt.plot(xa, ya,'rs', markersize=1)
    plt.show()
Main()