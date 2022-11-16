import numpy as np

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

A = [['02', '03', '01', '01'],
     ['01', '02', '03', '01'],
     ['01', '01', '02', '03'],
     ['03', '01', '01', '02']]


def hex2bin(hex_str, pad=0):
    bin = ''

    # każdy znak z otrzymanego ciągu zamieniam na odpowiadającą mu, binarną czwórkę
    for i in range(len(hex_str)):
        bin = bin + hex_to_bin[hex_str[i]]

    # usuwam zera z początku
    bin = bin.lstrip('0')

    # dopełniam ciąg zerami do wymaganej długości
    if len(bin) < pad:
        bin = '0' * (pad - len(bin)) + bin

    return bin


def bin2hex(bin_str, pad):
    # dopisuję 0 na początku, aby długość tekstu miała ilość znaków podzielną na 4
    if len(bin_str) % 4 == 1:
        bin_str = '000' + bin_str
    elif len(bin_str) % 4 == 2:
        bin_str = '00' + bin_str
    elif len(bin_str) % 4 == 3:
        bin_str = '0' + bin_str

    hex = ''

    i = len(bin_str)

    # biorę kolejne 4 znaki idąc od prawej strony i zamianiam na znak ze słownika
    while i > 1:
        hex_p = bin_to_hex[bin_str[i - 4:i]]
        hex = hex_p + hex
        i -= 4

    # dopełniam do wymaganej liczby znaków
    hex = hex.zfill(pad)

    return hex


def add_GF(p, q):
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


def multiply(p, q):
    multiplication_el = []
    n = 0

    # biore druga liczbe, przechodze od konca i mnoze - jesli elem = 1 - dodaje p z odpowiednia iloscia zer do tabeli,
    # jesli 0 - dodaje same zera
    for i in reversed(q):
        if i == '1':
            multiplication_el.append(p + n * '0')
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


def divide(p, q):
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
        elif abs(div[i]) % 2 == 0:
            div_f.append('0')
        elif abs(div[i]) % 2 != 0:
            div_f.append('1')
        else:
            div_f.append(str(int(div[i])))

    # jesli w wyniku dzielenia otrzymalem 2: dziele modulo 2 i podstawiam 0, -1 - zamieniam na 1
    for i in range(len(rest)):
        if abs(rest[i]) == 1:
            rest_f.append('1')
        elif abs(rest[i]) % 2 == 0:
            rest_f.append('0')
        elif abs(rest[i]) % 2 != 0:
            rest_f.append('1')
        else:
            rest_f.append(str(int(rest[i])))

    div = ''.join(div_f)
    rest = ''.join(rest_f)

    if rest == len(rest) * '0':
        rest = '0'

    return div, rest


def multiply_GF(p, q):
    irreducible = '100011011'

    # mnoże obie wartości
    mult_res = multiply(p, q)

    # jeśli wielomiany są tego samego stopnia lub dzielnik ma stopien mniejszy - dzielę
    if len(mult_res) >= len(irreducible):
        div, rest = divide(mult_res, irreducible)
    else:
        rest = mult_res

    return rest


def MixColumns(state):
    a = [['' for x in range(len(state))] for y in range(len(state[0]))]

    # zamieniam elementy z macierzy A na odpowiadajace im 8-el wartości binarne i wpisuje do macirzy a
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = hex2bin(A[i][j], 8)

    # zamieniam elementy z macierzy state na odpowiadajace im 8-el wartosci binarne
    for i in range(len(state)):
        for j in range(len(state[0])):
            state[i][j] = hex2bin(state[i][j], 8)

    result = [['0' for x in range(len(state))] for y in range(len(state[0]))]

    # wykonuje mnozenie a * state
    for i in range(len(state)):
        for j in range(len(a[0])):
            for k in range(len(a)):
                result[i][j] = add_GF(result[i][j], multiply_GF(a[i][k], state[k][j]))

    # otrzymane wartosci zamieniam na odpowiadajace im 2-el wartosci w systemie szesnastkowym
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = bin2hex(result[i][j], 2)

    return result


if __name__ == '__main__':
    print(MixColumns([['5a', '67', '2b', '3a'],
                      ['ba', '21', '82', '9e'],
                      ['e3', '86', '26', 'b5'],
                      ['01', '66', '09', '1a']]) ==
                     [['83', '4d', 'e4', '62'],
                      ['0a', 'd2', '57', 'c3'],
                      ['3e', 'fb', 'fe', 'fb'],
                      ['b5', 'c2', 'cb', '51']])