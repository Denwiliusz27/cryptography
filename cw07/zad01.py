import random

def DiffieHelman(g, p):
    a = random.randint(2, p-1)
    A = (g**a) % p

    b = random.randint(2, p-1)
    B = (g**b) % p

    k_B = (A**b) % p
    k_A = (B**a) % p

    print("k_B: ", k_B)
    print("k_A: ", k_A)


if __name__ == '__main__':
    DiffieHelman(5, 23)