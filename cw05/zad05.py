import textwrap

rci = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

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


if __name__ == '__main__':
    key = '10111101101101001100100101100001111111111100001110000101100001110111010001010001101011111111111000011100111010011000101011100110'
    print(KeyExpansion(key) ==
          [[['bd', 'b4', 'c9', '61'],
            ['ff', 'c3', '85', '87'],
            ['74', '51', 'af', 'fe'],
            ['1c', 'e9', '8a', 'e6']],
           [['a2', 'ca', '47', 'fd'],
            ['5d', '09', 'c2', '7a'],
            ['29', '58', '6d', '84'],
            ['35', 'b1', 'e7', '62']],
           [['68', '5e', 'ed', '6b'],
            ['35', '57', '2f', '11'],
            ['1c', '0f', '42', '95'],
            ['29', 'be', 'a5', 'f7']],
           [['c2', '58', '85', 'ce'],
            ['f7', '0f', 'aa', 'df'],
            ['eb', '00', 'e8', '4a'],
            ['c2', 'be', '4d', 'bd']],
           [['64', 'bb', 'ff', 'eb'],
            ['93', 'b4', '55', '34'],
            ['78', 'b4', 'bd', '7e'],
            ['ba', '0a', 'f0', 'c3']],
           [['13', '37', 'd1', '1f'],
            ['80', '83', '84', '2b'],
            ['f8', '37', '39', '55'],
            ['42', '3d', 'c9', '96']],
           [['14', 'ea', '41', '33'],
            ['94', '69', 'c5', '18'],
            ['6c', '5e', 'fc', '4d'],
            ['2e', '63', '35', 'db']],
           [['af', '7c', 'f8', '02'],
            ['3b', '15', '3d', '1a'],
            ['57', '4b', 'c1', '57'],
            ['79', '28', 'f4', '8c']],
           [['1b', 'c3', '9c', 'b4'],
            ['20', 'd6', 'a1', 'ae'],
            ['77', '9d', '60', 'f9'],
            ['0e', 'b5', '94', '75']],
           [['d5', 'e1', '01', '1f'],
            ['f5', '37', 'a0', 'b1'],
            ['82', 'aa', 'c0', '48'],
            ['8c', '1f', '54', '3d']],
           [['23', 'c1', '26', '7b'],
            ['d6', 'f6', '86', 'ca'],
            ['54', '5c', '46', '82'],
            ['d8', '43', '12', 'bf']]])
