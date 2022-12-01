import numpy as np
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


def inv(p, n):
    if np.isnan(p):
        return float('nan')

    if p == 0:
        return float('nan')

    t = 1
    newt = 0
    r = 0
    newr = 1

    while n != 0:
        q = p // n
        t, newt = newt, t - (q * newt)
        r, newr = newr, r - (q * newr)
        p, n = n, p % n

    if t < 0:
        t += newt

    return t


# dodawanie punktu P i Q
def add(P, Q, a, p):
    px = P[0]
    py = P[1]
    qx = Q[0]
    qy = Q[1]

    if P == Q:
        # jeśli punkty mają te same współrzędne i py != 0, obliczane jest s
        if py != 0:
            s = (3 * ((px) ** 2) + a) * inv(2 * py, p)
        # jeśli py = 0 (dzielenie przez zero) - zwracany jest ['nan', 'nan']
        else:
            return [float('nan'), float('nan')]
    # jeśli punkt P jest ['nan', 'nan'], zwracam Q jako wynik
    elif np.isnan(px) and np.isnan(py):
        return Q
    # jeśli punkt Q jest ['nan', 'nan'], zwracam P jako wynik
    elif np.isnan(qx) and np.isnan(qy):
        return P
    else:
        # jeśli różnica qx i px jest różna od 0, obliczam s
        if (qx - px) != 0:
            s = (qy - py) * inv(qx - px, p)
        # w przeciwym wypadku mamy dzielenie przez 0 - zwracam ['nan', 'nan']
        else:
            return [float('nan'), float('nan')]

    s = s % p

    # obliczam x i y punktu wynikowego
    x = (s ** 2 - px - qx) % p
    y = (s * (px - x) - py) % p

    return [x, y]


# mnożenie punktu P razy n
def multiply(n, P, a, p):
    new_P = P

    # sprawdzam czy P nie jest elementem w nieskończoności
    if np.isnan(P[0]) and np.isnan(P[1]):
        return new_P

    for i in range(1, n):
        new_P = add(new_P, P, a, p)

    return new_P


def analize(a, b, p):
    points = gen(a, b, p)
    print(points)

    x = []
    y = []

    for i in range(len(points)):
        px = points[i][0]
        py = points[i][1]
        x.append(px)
        y.append(py)

    x = np.array(x)
    y = np.array(y)

    # N = len(x)
    # colors = np.random.rand(N)
    # area = (30 * np.random.rand(N)) ** 2

    plt.scatter(x, y)
    plt.show()

    for i in range(len(points)):
        j = 1
        new_p = points[i]
        add_point = 1

        while (add_point):
            print(j, "* [", points[i][0], ", ", points[i][1], "] --> ", "[", new_p[0], ", ", new_p[1], "]")
            add_point = input("Dodac kolejna wartosc?: ")

            if add_point == '1':
                j += 1
                point = [int(points[i][0]), int(points[i][1])]
                # print("j:", j, ", P:", point, ", a:", a, ", p:",p)
                new_p = multiply(j, point, a, p)
            else:
                add_point = 0

        print("[", points[i][0], ", ", points[i][1], "]  generuje ", j, " elementowa grupe")


if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~       y^2 = x^3 - x     ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    analize(-1, 0, 7)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~    y^2 = x^3 - 2x + 1   ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    analize(-2, 1, 5)