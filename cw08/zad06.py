import random
import numpy as np


# generuje liste punktów krzywej eliptycznej dla podanego a, b i p
def gen(a,b,p):
    result = []

    for x in range(p):
        for y in range(p):
            L = (y**2) % p
            P = (x**3 + a*x + b) % p
            # sprawdzenie czy punkt x,y spełnia nierówność y^3 = (x^2 + ax + b) % p
            if L == P:
                result.append([x, y])

    return result


# zwraca rząd punktu G
def ord(G,a,p):
    new_G = G

    # sprawdzam czy G nie jest elementem w nieskończoności
    if np.isnan(G[0]) and np.isnan(G[1]):
        return new_G

    # rząd elementu G
    n = 1

    # dodaje G dopóki new_G nie będzie elementem w nieskończoności
    while not (np.isnan(new_G[0]) and np.isnan(new_G[1])):
        new_G = add(new_G, G, a, p)
        n += 1

    return n


# znajduje punkt z największym rzędem
def findMax(a, b, p):
    points = gen(a, b, p)

    max = 0
    for i in range(len(points)):
        value = ord(points[i], a, p)

        if value > max:
            max = value
            point = points[i]

    return max, point


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


if __name__ == '__main__':
    a = -1
    b = 0
    p = 97
    max, G = findMax(a, b, p)

    points = gen(a, b, p)

    n = random.randint(2, len(points)-1)
    A = multiply(n, G, a, p)

    m = random.randint(2, len(points)-1)
    B = multiply(m, G, a, p)

    k_A = multiply(n, B, a, p)
    k_B = multiply(m, A, a, p)

    print(k_A == k_B)