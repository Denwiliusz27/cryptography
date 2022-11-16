
hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

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


def xor(bin_str1, bin_str2):
    bin_xor = ''

    for i in range(len(bin_str1)):
        if bin_str1[i] == bin_str2[i]:
            bin_xor += '0'
        else:
            bin_xor += '1'

    return bin_xor


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


if __name__ == '__main__':
    print(AddRoundKey([['83', '4d', 'e4', '62'],
                       ['0a', 'd2', '57', 'c3'],
                       ['3e', 'fb', 'fe', 'fb'],
                       ['b5', 'c2', 'cb', '51']],
                      [['23', 'c1', '26', '7b'],
                       ['d6', 'f6', '86', 'ca'],
                       ['54', '5c', '46', '82'],
                       ['d8', '43', '12', 'bf']])==
                      [['a0', '8c', 'c2', '19'],
                       ['dc', '24', 'd1', '09'],
                       ['6a', 'a7', 'b8', '79'],
                       ['6d', '81', 'd9', 'ee']])
