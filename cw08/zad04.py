import math
from sympy import primerange
import matplotlib.pyplot as plt

# generuje liste punktów krzywej eliptycznej dla podanego a, b i p
def gen(a, b, p):
    result = []

    for x in range(p):
        for y in range(p):
            L = (y ** 2) % p
            P = (x ** 3 + a * x + b) % p
            # sprawdzenie czy punkt x,y spełnia nierówność y^3 = (x^2 + ax + b) % p
            if L == P:
                result.append([x, y])

    return result


if __name__ == '__main__':
    values = list(primerange(0, 100))
    a = -1
    b = 0
    p = []
    nr_points = []

    # obiczam p i opowiadającą mu liczbe punktów
    for i in range(len(values)):
        test_p = values[i]
        p.append(test_p)

        points = gen(a, b, test_p)
        nr_points.append(len(points))

    top = []
    down = []

    f_points = [0] + p

    # obliczam wartości funkcji dla kolejnych wartości p
    for n in range(len(f_points)):
        top.append(f_points[n] + 1 + 2 * math.sqrt(f_points[n]))
        down.append(f_points[n] + 1 - 2 * math.sqrt(f_points[n]))

    plt.plot(top, f_points, 'r', label='p + 1 + 2 * math.sqrt(p)')
    plt.plot(down, f_points, 'g', label='p + 1 - 2 * math.sqrt(p)')

    # plt.bar(nr_points, p, width=2.0)
    plt.plot(nr_points, p, 'o')
    plt.xticks(nr_points, nr_points)
    plt.yticks(p, p)
    # plt.grid()
    plt.xlabel('nr of points')
    plt.ylabel('p value')
    plt.show()
