import hashlib, os, binascii
import random


def simple_hash(str):
    m = hashlib.sha256()
    m.update(bytes(int(str, 16)))
    return m.hexdigest()[:2]


def rho_pollard():
    h1 = str(binascii.b2a_hex(os.urandom(random.randint(1, 5))))[2:-1]
    h1p = h1

    print("liczba: ", h1)

    h2 = simple_hash(h1)
    h2p = simple_hash(simple_hash(h1p))

    i = 1
    while h2 != h2p:
        h1 = h2
        h1p = h2p

        h2 = simple_hash(h1)
        h2p = simple_hash(simple_hash(h1p))
        i += 1

    print("index: ", i)
    print("h1 = ", str(h1))
    print("h1p = ", str(h1p))


if __name__ == '__main__':
    rho_pollard()
