import textwrap
import numpy as np

rci = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

A = [['02', '03', '01', '01'],
     ['01', '02', '03', '01'],
     ['01', '01', '02', '03'],
     ['03', '01', '01', '02']]

SBox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
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


def bin2dec(bin_str):
    dec_val = 0

    for i in range(0, len(bin_str)):
        if bin_str[i] == '1':
            dec_val += 2 ** (len(bin_str) - i - 1)

    return dec_val


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


def xor(bin_str1, bin_str2):
    bin_xor = ''

    for i in range(len(bin_str1)):
        if bin_str1[i] == bin_str2[i]:
            bin_xor += '0'
        else:
            bin_xor += '1'

    return bin_xor


# przesuwa elementy słowa o 1 w lewo
def RotWord(state):
    return state[1:] + state[:1]


# robi SBox na elementach słowa
def SubWord(word):
    result = ['' for i in range(len(word))]

    for i in range(len(word)):
        first = word[i][0]
        last = word[i][1]

        row = bin2dec(hex_to_bin[first])
        col = bin2dec(hex_to_bin[last])

        result[i] = SBox[row][col]

    return result


# robi xor na dwoch podanych slowach
def Rcon(word, rci_1):
    # tworzy tablice stworzona z podanego elem. rci oraz zer
    b_rci = ['00' for i in range(len(word))]
    b_rci[0] = rci_1

    # zamienia slowo rci na wersje binarna
    for i in range(len(b_rci)):
        b_rci[i] = hex2bin(b_rci[i], 8)

    # zamienia slowo na wersje binarna
    b_word = ['' for i in range(len(word))]
    for i in range(len(word)):
        b_word[i] = hex2bin(word[i], 8)

    # wykonuje xor dla dwoch odpowiadajacych sobie elem. z podanyh slow, robi xor i zwraca wartosc hex
    result = ['' for i in range(len(word))]
    for i in range(len(result)):
        result[i] = xor(b_rci[i], b_word[i])
        result[i] = bin2hex(result[i], 2)

    return result


def prepare_state(msg):
    div_msg = textwrap.wrap(msg, 8)
    matrix = []
    row = []

    for i in range(len(div_msg)):
        if i % 4 == 0 and i != 0:
            matrix.append(row)
            row = []

        msg = div_msg[i]
        msg1 = msg[0:int(len(msg) / 2)]
        msg2 = msg[int(len(msg) / 2):len(msg)]

        b = bin_to_hex[msg1] + bin_to_hex[msg2]
        row.append(b)

    matrix.append(row)
    return matrix


# dla podanych dwoch slow hex robi xor i zwraca wynik
def hex_xor(word1, word2):
    result = ['' for i in range(len(word1))]

    for i in range(len(word1)):
        b_word1 = hex2bin(word1[i], 8)
        b_word2 = hex2bin(word2[i], 8)
        result[i] = xor(b_word1, b_word2)
        result[i] = bin2hex(result[i], 2)

    return result


def KeyExpansion(key):
    # generuje podklucze i wstawiam je jako pierwszy wiersz tablicy wynikowej
    start_words = prepare_state(key)
    subkeys = [[] for i in range(11)]
    subkeys[0] = start_words[:]

    for i in range(0, 10):
        # biorę ostatnie slowo z ostatniej listy slow i przesuwam go o 1 bajt w lewo
        rot_word = RotWord(subkeys[i][len(subkeys[i][0]) - 1])

        # robie SBox na otrzymanym slowie
        sub_word = SubWord(rot_word)

        # do otrzymanego slowa dodaje odpowiedni rci
        rcon = Rcon(sub_word, rci[i])

        # dodaje otrzymane slowo jako pierwszy element kolejnego wiersza slow
        subkeys[i + 1].append(hex_xor(rcon, subkeys[i][0]))

        # generje pozostale slowa
        for j in range(1, 4):
            subkeys[i + 1].append(hex_xor(subkeys[i][j], subkeys[i + 1][j - 1]))

    return subkeys


def ShiftRows(state):
    result = []

    for i in range(0, len(state)):
        # dodaje pierwszy wiersz bez przesuniecia
        if i == 0:
            result.append(state[0])
        # dodaje reszte wierszy - kazdy koleny przesuwam o 1 więcej niż przedni
        else:
            row = state[i][i:len(state)] + state[i][0:i]
            result.append(row)

    return result


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


def SubBytes(state):
    # pobieram ilosc kolumn i wierszy state
    rows = len(state)
    columns = len(state[0])

    # tworze tabele wynikową z odpowiednia iloscia wierszy i kolumn
    result = [['' for x in range(rows)] for y in range(columns)]

    for i in range(rows):
        for j in range(columns):
            # pobieram pierwszy znak odczytanego ciagu
            first = state[i][j][0]
            # pobieram drugi element odczytanego ciagu
            last = state[i][j][1]

            # pierwszy element zamieniam na odpowiadajaca mu wartosc w syst. dziesietnym = nr wiersza
            row = bin2dec(hex_to_bin[first])
            # drugi element zamieniam na odpowiadajaca mu wartosc w syst. dziesietnym = nr kolumny
            col = bin2dec(hex_to_bin[last])

            result[i][j] = SBox[row][col]

    return result


def AddRoundKey(state, subkey):
    final = []

    # biorę odpowiadajace sobie elementy z obu tabel
    for i in range(len(state)):
        result = []
        state_b = []
        subkey_b = []

        for j in range(len(state[i])):
            # pobrane elementy zamienam na bity
            state_b.append(hex2bin(state[i][j], 8))
            subkey_b.append(hex2bin(subkey[i][j], 8))

            # wykonuje xor na podanych elementach
            temp = xor(state_b[j], subkey_b[j])

            # wynik xora zamieniam na hex i dodaje do tabeli wynikowej
            result.append(bin2hex(temp, 2))

        final.append(result)

    return final


def AES(msg, subkeys):
    state = prepare_state(msg)
    state = AddRoundKey(state, subkeys[0])

    for i in range(1, 10):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, subkeys[i])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, subkeys[10])

    result = ''

    for i in range(len(state)):
        for j in range(len(state[i])):
            result += hex2bin(state[i][j], 8)

    return result


if __name__ == '__main__':
    msg = '01000110000010100000101110100010110111111100000001111011000100010010001111010010010011011101110011010011010000000100001100001001'
    key = '10111101101101001100100101100001111111111100001110000101100001110111010001010001101011111111111000011100111010011000101011100110'

    subkeys = KeyExpansion(key)
    print(AES(msg,
              subkeys) == '10011011111001010110001100111101110001011011101000011101001000001010111100001110011000010000111101111000010101011111010000001101')
