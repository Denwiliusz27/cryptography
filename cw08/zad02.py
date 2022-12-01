import numpy as np


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

    s = 0

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
    print("Dodawanie:")
    print(add([4, 2], [5, 1], -1, 7) == [6, 0])
    print(add([4, 2], [4, 2], -1, 7) == [1, 0])
    print(add([4, 2], [5, 1], -1, 7) == [6, 0])
    print(add([4, 2], [float('nan'), float('nan')], -1, 7) == [4, 2])
    print(np.isnan(add([float('nan'), float('nan')], [float('nan'), float('nan')], -1, 7)))
    print(np.isnan(add([0, 0], [0, 0], -1, 7)))
    print(add([2, 0], [3, 2], 0, 5) == [4, 1])
    print(np.isnan(add([2, 0], [2, 0], 0, 5)))

    print("~~~~~~~~~~~~~~~~")
    print("Mnożenie:")
    print(multiply(1, [4, 2], -1, 7) == [4, 2])
    print(multiply(1, [4, 2], -1, 7) == [4, 2])
    print(multiply(3, [4, 2], -1, 7) == [4, 5])
    print(np.isnan(multiply(4, [4, 2], -1, 7)))
    print(np.isnan(multiply(2, [float('nan'), float('nan')], -1, 7)))
    print(multiply(5, [2, 0], 0, 5) == [2, 0])
    print(multiply(5, [3, 3], 0, 5) == [3, 2])
