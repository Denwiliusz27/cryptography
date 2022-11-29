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


if __name__ == '__main__':
    print(pow_mod(7, 3, 2) == 1)
    print(pow_mod(2, 1024, 7) == 2)
    print(pow_mod(3, 10 ** 100, 7) == 4)
    print(pow_mod(3 ** 99, 10 ** 100, 7) == 1)