import textwrap

E = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11,
     12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22,
     23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

SBox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

P = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1,
     7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]


def permute(k, perm):
    permuted = ''

    for i in range(len(perm)):
        permuted += k[perm[i]]

    return permuted


def xor(bin_str1, bin_str2):
    bin_xor = ''

    for i in range(len(bin_str1)):
        if bin_str1[i] == bin_str2[i]:
            bin_xor += '0'
        else:
            bin_xor += '1'

    return bin_xor


def bin2dec(bin_str):
    dec_val = 0

    for i in range(0, len(bin_str)):
        if bin_str[i] == '1' :
            dec_val += 2**(len(bin_str)-i-1)

    return dec_val


def dec2bin(dec_str, pad):
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


def F(right, subkey):
    # permutacja E
    right_e = permute(right, E)

    #xor wyniku permuacji oraz klucza
    right_xor = xor(right_e, subkey)

    #podział otrzymanego ciągu na 8 podciagów po 6 elementów
    sboxes = textwrap.wrap(right_xor, 6)

    sboxes_str = ''

    for i in range(0, len(sboxes)):
        elem = sboxes[i]

        # pobranie pierwszgo i ostatniego elementu
        first_last = elem[0] + elem[5]

        # obliczenie numeru wiersza
        row_nr = bin2dec(first_last)

        # pobranie środkowego ciągu
        middle = elem[1:5]

        # zamiana ciągu na nr kolumny
        column_nr = bin2dec(middle)

        # pobranie odpowiedniego elementu z macierzy SBox
        sbox_bin = SBox[i][row_nr][column_nr]

        # zamiana odczytanej liczby na binarną
        sboxes[i] = dec2bin(sbox_bin, 4)
        sboxes_str += sboxes[i]

    final = permute(sboxes_str, P)

    return final



if __name__ == '__main__':
    print(F('11001101000100110010010100110110', '000110010100110011010000011100101101111010001100')
          == '00010000110101100001010011011100')
    print(F('00010010001101000101011010101011', '010001010110100001011000000110101011110011001110')
           == '10110011111110000011101011101011')