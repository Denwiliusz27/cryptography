import random


def dec2bin(dec_str):
    return bin(dec_str).replace("0b", "")


def pow_mod(x, n, m):
    p = 1

    # zamieniam n na zapis bitowy
    n_b = dec2bin(n)

    # pętla po wszystkich bitach
    for i in range(len(n_b)):
        # ustawiam p jako p^2 mod m
        p = (p ** 2) % m

        # jeśli sprawdzany bit jest == 1
        if n_b[i] == '1':
            # # ustawiam p = x^n mod m
            p = (p * x) % m

    return p


def gen_p(a, b):
    while (1):
        # losuje wartość z podanego przedziału
        value = random.randint(a, b)

        # sprawdzam czy wylosowana wartość jest liczbą pierwszą
        if Fermat_test(value, 10):
            # jeśli znaleziona wartość jest liczbą pierwszą, zwracam ją
            return value


def Fermat_test(p, k):
    if (p - 2) < 2:
        return False

    # sprawdzam k razy
    for i in range(k):
        # losuje liczbe z przedziału [2, p-2]
        a = random.randint(2, p - 2)

        # sprawdzam czy a^(p-1) mod p != 1
        if pow_mod(a, p-1, p) != 1:
            return False

    return True


if __name__ == '__main__':
    print(Fermat_test(71, 10) == True)
    print(Fermat_test(41, 10) == True)
    print(Fermat_test(62, 10) == False)
    print(Fermat_test(84, 10) == False)

    print("~~~~~~~~~~~~~~~~~")
    print("Gen value: ", gen_p(1, 100))
