import random
import numpy as np

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


def key_gen(p,q):
    n = p*q

    # obliczam funkce Eulera
    qn = (q-1)*(p-1)

    e = 65537 #gen_p(1, qn-1)

    # obliczam d jako odwrotność e w ciele Z
    d = inv(e, qn)

    return (n, e, d)


if __name__ == '__main__':
    p = 24130780476900131841553779066939443255102203937160657723394451174808141403858935238883126295228560935516885174421847238379397184900972008801015315248328437
    q = 26660613491521684005574100352062919789979599401844483402246984186988668019447679726081352452799126206997555710356464145743285983450292024894053538317854159

    print(key_gen(p, q) == (
        643341411543391711051425916925550311012265711300705520200325675109446836493100912341600261266222036750541155307483726185012838542757173209246878527615686866322037404779287199511097525538499079836420404197380885254900993985365780000028685663116338197119892656788379026665075201747282243427197060237417498419483,
        65537,
        334692241429603741219438891581498052305769251366366399304669177607406348936208181733781847015759652456012644616150535488014598320266503205353805078033123914361616918116605669461614375732022492713408743728419283824726654095683796656269600488579712785553345684168299073769307373555258299179136288438930486131753))
