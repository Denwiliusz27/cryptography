def inv(p, n):
    t = 0
    newt = 1
    r = n
    newr = p

    while newr != 0 :
        q = r // newr
        t, newt = newt, t - (q * newt)
        r, newr = newr, r - (q * newr)

    if r > 1:
        return 0
    if t < 0:
        t += n

    return t


if __name__ == '__main__':
    print(inv(5, 7) == 3)
    print(inv(3, 2) == 1)
    print(inv(5, 7) == 3)
    print(inv(3, 11) == 4)