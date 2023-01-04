import numpy as np
import hashlib

hex_to_bin = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111' }

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}


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


def key_gen(p, q):
    n = p*q
    e = 65537

    # obliczam funkce Eulera
    qn = (q-1)*(p-1)

    # obliczam d jako odwrotność e w ciele Z
    d = inv(e, qn)

    return (n, e, d)


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


def enc(x,e,n):
    # wykonuje potęgowanie modulo
    return pow_mod(x, e, n)


def dec(y,d,n):
    # wykonuje potęgowanie modulo
    return pow_mod(y, d, n)


def decrypt(sign, d, n):
    return hex(enc(int(sign, base=16), d, n))[2:]


# generuje podpis elektroniczny pliku dla klucza prywatnego e i n
def sign(file_name, e, n):
    file = open(file_name, 'rb')
    data = file.read()

    object = hashlib.sha256()
    object.update(data)

    # zamieniam hex z pliku na int
    hash = int(object.hexdigest(), base=16)

    # wykorzystuje funkcje do szyfracji
    return hex(enc(hash, e, n))[2:]


# sprawdza autentyczność podpisu
def check_sign(file_name, d, n, s):
    file = open(file_name, 'rb')
    data = file.read()

    object = hashlib.sha256()
    object.update(data)

    # sprawdzam czy deszyfracja s daje to samo co hex z pliku
    if object.hexdigest() == decrypt(s, d, n):
        return True
    else:
        return False


if __name__ == '__main__':
    p=24130780476900131841553779066939443255102203937160657723394451174808141403858935238883126295228560935516885174421847238379397184900972008801015315248328437
    q=26660613491521684005574100352062919789979599401844483402246984186988668019447679726081352452799126206997555710356464145743285983450292024894053538317854159

    n, e, d = key_gen(p, q)

    print(sign('correlation.png', e,
               n) == '1d5e7cd47f75b13159a37c8ffb3ba7d9f43a21f4758ae06e856da0a468fd1772f7b8b52d0f948fd02610e0e05a54c0fff12d7bd27575583cfdf53b124e9c0e95df1de156aa0af52239f1329ab69000b4a6a61d3d45f190c4b9df4ca4b7d30904162727353a8fb09c9faf847eeb0f6f65394d92cb57ced2cdcff36c444394e3fff')
    print(sign('Campin_Boze_Narodzenie1.png', e,
               n) == '1c6097177871bb4873fcd0ae658d28f46fcc54e4b0e595954a57c0008f8b86c7427cecf28296240025941fe2a019b80fcc5f43c4cae6b1d2163cecf8438336d3da6e33ae326dfa2c0e5ea7bbad511dd140bc7b0cd34829623bfd02bc66bc9b43d57443b7fd950bea5cb5f5df99d8611eeb0d4458b19809e3ff86abf6538c3e453')

    print(check_sign('correlation.png', d, n,
                     '1d5e7cd47f75b13159a37c8ffb3ba7d9f43a21f4758ae06e856da0a468fd1772f7b8b52d0f948fd02610e0e05a54c0fff12d7bd27575583cfdf53b124e9c0e95df1de156aa0af52239f1329ab69000b4a6a61d3d45f190c4b9df4ca4b7d30904162727353a8fb09c9faf847eeb0f6f65394d92cb57ced2cdcff36c444394e3fff') == True)
    print(check_sign('correlation.png', d, n,
                     '1d5e7cd47f75b13159a37c8ffb3ba7d9f43a21f4758ae06e856ba0a468fd1772f7b8b52d0f948fd02610e0e05a54c0fff12d7bd27575583cfdf53b124e9c0e95df1de156aa0af52239f1329ab69000b4a6a61d3d45f190c4b9df4ca4b7d30904162727353a8fb09c9faf847eeb0f6f65394d92cb57ced2cdcff36c444394e3fff') == False)
    print(check_sign('Campin_Boze_Narodzenie1.png', d, n,
                     '1c6097177871bb4873fcd0ae658d28f46fcc54e4b0e595954a57c0008f8b86c7427cecf28296240025941fe2a019b80fcc5f43c4cae6b1d2163cecf8438336d3da6e33ae326dfa2c0e5ea7bbad511dd140bc7b0cd34829623bfd02bc66bc9b43d57443b7fd950bea5cb5f5df99d8611eeb0d4458b19809e3ff86abf6538c3e453') == True)
    print(check_sign('Campin_Boze_Narodzenie1.png', d, n,
                     '1c6097177871bb4873fcd0ae658d28f46fec54e4b0e595954a57c0008f8b86c7427cecf28296240025941fe2a019b80fcc5f43c4cae6b1d2163cecf8438336d3da6e33ae326dfa2c0e5ea7bbad511dd140bc7b0cd34829623bfd02bc66bc9b43d57443b7fd950bea5cb5f5df99d8611eeb0d4458b19809e3ff86abf6538c3e453') == False)
