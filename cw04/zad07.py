import numpy as np

bin_to_hex = { '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
                '1000':'8', '1001':'9', '1010':'a', '1011':'b', '1100':'c', '1101':'d', '1110':'e', '1111':'f' }


SBox=[['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
      ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
      ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
      ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
      ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
      ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
      ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
      ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
      ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
      ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
      ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
      ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
      ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
      ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
      ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
      ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

A=[[1, 1, 1, 1, 1, 0, 0, 0],
   [0, 1, 1, 1, 1, 1, 0, 0],
   [0, 0, 1, 1, 1, 1, 1, 0],
   [0, 0, 0, 1, 1, 1, 1, 1],
   [1, 0, 0, 0, 1, 1, 1, 1],
   [1, 1, 0, 0, 0, 1, 1, 1],
   [1, 1, 1, 0, 0, 0, 1, 1],
   [1, 1, 1, 1, 0, 0, 0, 1]]

v=[0, 1, 1, 0, 0, 0, 1, 1]


def bin2hex(bin_str, pad):
    # dopisuję 0 na początku, aby długość tekstu miała ilość znaków podzielną na 4
    if len(bin_str)%4 == 1:
        bin_str = '000' + bin_str
    elif len(bin_str)%4 == 2:
        bin_str = '00' + bin_str
    elif len(bin_str)%4 == 3:
        bin_str = '0' + bin_str

    hex = ''
    i = len(bin_str)

    # biorę kolejne 4 znaki idąc od prawej strony i zamianiam na znak ze słownika
    while i > 1:
        hex_p = bin_to_hex[bin_str[i-4:i]]
        hex = hex_p + hex
        i -= 4

    # dopełniam do wymaganej liczby znaków
    hex = hex.zfill(pad)

    return hex


def add_GF(p,q):
    sum = '0'

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


def EEA_GF(a, b):
    x = '1'
    y = '0'
    r = '0'
    s = '1'

    while b != '0':
        a = a.lstrip('0')
        b = b.lstrip('0')
        q, c = divide(a, b)

        a = b
        b = c

        r2 = r
        s2 = s
        r = add_GF(x, multiply_GF(q, r))
        s = add_GF(y, multiply_GF(q, s))

        x = r2
        y = s2

    return x, y


def inverse_GF(p):
    m = '100011011'

    s, t = EEA_GF(p, m)

    return s


def substitute(p):
    if p == '00000000':
        p1 = '00000000'
    else:
        p1 = inverse_GF(p)

    p1_arr = []

    # dopełniam zerami otrzymany ciąg żeby był dł = 8
    if len(p1) < 8:
        p1 = '0' * (8 - len(p1)) + p1

    # zamieniam otrzymany ciąg na wertok
    for i in range(len(p1)):
        if p1[i] == '0':
            p1_arr.append(0)
        else:
            p1_arr.append(1)

    ap1 = ['0', '0', '0', '0', '0', '0', '0', '0']

    # mnoże macierz A z p
    for i in range(0, len(A)):
        for j in range(len(p1_arr)):
            ap1[i] = add_GF(ap1[i], multiply_GF(str(A[i][j]), p1[j]))

    q = ['0', '0', '0', '0', '0', '0', '0', '0']

    # obliczam q przez dodanie do Ap v
    for i in range(len(ap1)):
        q[i] = add_GF(ap1[i], str(v[i]))

    return bin2hex(''.join(q), 2)


def dec2bin(dec_str, pad=4):
    bin_val = ['0'] * pad
    bin_val_final = ''
    i = pad-1

    while dec_str >= 1:
        reminder = dec_str % 2
        if reminder == 1:
            bin_val[i] = '1'

        dec_str = dec_str // 2
        i -= 1

    for n in range(0, len(bin_val)):
         bin_val_final = bin_val_final + bin_val[n]

    return bin_val_final



if __name__ == '__main__':
    print("Substitute:")
    print(substitute('11010101') == '03')
    print(substitute('01010001') == 'd1')
    print(substitute('11011101') == 'c1')
    print(substitute('11101100') == 'ce')

    s_box = [['' for x in range(16)] for y in range(16)]

    for i in range(0, 16):
        for j in range(0, 16):
            bin = dec2bin(i) + dec2bin(j)
            val = substitute(bin)
            s_box[i][j] = val

    print("\ns_box:")
    print(s_box == SBox)