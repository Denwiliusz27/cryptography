import numpy as np

hex_to_bin = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111' }

A=[['02','03','01','01'],
   ['01','02','03','01'],
   ['01','01','02','03'],
   ['03','01','01','02']]


def hex2bin(hex_str,pad=0):
    bin = ''

    # każdy znak z otrzymanego ciągu zamieniam na odpowiadającą mu, binarną czwórkę
    for i in range(len(hex_str)):
        bin = bin + hex_to_bin[hex_str[i]]

    # usuwam zera z początku
    bin = bin.lstrip('0')

    # dopełniam ciąg zerami do wymaganej długości
    if len(bin) < pad:
        bin = '0'* (pad-len(bin)) + bin

    return bin


def add_GF(p,q):
    sum = ''

    if len(p) > len(q):
        b_len = len(p)
    else:
        b_len = len(q)

    # dopełniam oba ciągi zerami, aby kazdy miał po 3 znaki
    p = p.zfill(b_len)
    q = q.zfill(b_len)

    for i in range(b_len):
        if p[i] == q[i]:
            sum += '0'
        else:
            sum += '1'

    # pozbywam sie wiodących zer
    sum = sum.lstrip('0')

    if sum == '':
        sum = '0'

    return sum


def multiply(p,q):
    multiplication_el = []
    n = 0

    # biore druga liczbe, przechodze od konca i mnoze - jesli elem = 1 - dodaje p z odpowiednia iloscia zer do tabeli,
    # jesli 0 - dodaje same zera
    for i in reversed(q):
        if i == '1':
            multiplication_el.append(p + n *'0')
        else:
            multiplication_el.append(len(p) * '0')
        n += 1

    sum = ''

    # dodaje elementy z tabeli do siebie i otrzymuje wynik koncowy
    if len(multiplication_el) > 1:
        sum = add_GF(multiplication_el[0], multiplication_el[1])

        if len(multiplication_el) > 2:
            for i in range(2, len(multiplication_el)):
                sum = add_GF(sum, multiplication_el[i])
    else:
        sum = multiplication_el[0]

    return sum


def divide(p,q):
    p_array = []
    q_array = []

    # zamieniam ciagi na elementy w tabelach
    for i in range(len(p)):
        p_array.append(int(p[i]))

    for i in range(len(q)):
        q_array.append(int(q[i]))

    p_array = np.array(p_array)
    q_array = np.array(q_array)

    # uzywam funkcji do dzielenia wielomianow
    div, rest = np.polydiv(p_array, q_array)

    div_f = []
    rest_f = []

    # jesli w wyniku dzielenia otrzymalem 2: dziele modulo 2 i podstawiam 0, -1 - zamieniam na 1
    for i in range(len(div)):
        if abs(div[i]) == 1:
            div_f.append('1')
        elif abs(div[i])%2 == 0:
            div_f.append('0')
        elif abs(div[i])%2 != 0:
            div_f.append('1')
        else:
            div_f.append(str(int(div[i])))

    # jesli w wyniku dzielenia otrzymalem 2: dziele modulo 2 i podstawiam 0, -1 - zamieniam na 1
    for i in range(len(rest)):
        if rest[i] == -1:
            rest_f.append('1')
        elif abs(rest[i])%2 == 0:
            rest_f.append('0')
        elif abs(rest[i])%2 != 0:
            rest_f.append('1')
        else:
            rest_f.append(str(int(rest[i])))

    div = ''.join(div_f)
    rest = ''.join(rest_f)

    if rest == len(rest) * '0':
        rest = '0'

    return div, rest


def multiply_GF(p,q):
    irreducible = '100011011'

    # mnoże obie wartości
    mult_res = multiply(p,q)

    # jeśli wielomiany są tego samego stopnia lub dzielnik ma stopien mniejszy - dzielę
    if len(mult_res) >= len(irreducible):
        div, rest = divide(mult_res, irreducible)
    else:
        rest = mult_res

    return rest


def MixColumns(state):
    a = [['' for x in range(len(state))] for y in range(len(state[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = hex2bin(A[i][j], 8)

    print(a)


    for i in range(len(state)):
        for j in range(len(state[0])):
            state[i][j] = hex2bin(state[i][j],8)

    print(state)






if __name__ == '__main__':
    print(MixColumns([['5a', '67', '2b', '3a'],
                      ['ba', '21', '82', '9e'],
                      ['e3', '86', '26', 'b5'],
                      ['01', '66', '09', '1a']]) ==
                     [['83', '4d', 'e4', '62'],
                      ['0a', 'd2', '57', 'c3'],
                      ['3e', 'fb', 'fe', 'fb'],
                      ['b5', 'c2', 'cb', '51']])