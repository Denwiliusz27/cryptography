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


if __name__ == '__main__':
    print(inv(5, 7) == 3)
    print(inv(3, 2) == 1)
    print(inv(5, 7) == 3)
    print(inv(3, 11) == 4)