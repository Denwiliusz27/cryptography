
PC1 = [56, 48, 40, 32, 24, 16,  8,  0, 57, 49, 41, 33, 25, 17,  9,  1, 58,
       50, 42, 34, 26, 18, 10,  2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22,
       14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 60, 52, 44, 36, 28, 20, 12,
        4, 27, 19, 11,  3]

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

PC2 = [13, 16, 10, 23,  0,  4,  2, 27, 14,  5, 20,  9, 22, 18, 11,  3,
       25, 7, 15,  6, 26, 19, 12,  1, 40, 51, 30, 36, 46, 54, 29, 39,
       50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]


def permute(k, perm):
    permuted = ''

    for i in range(len(perm)):
        permuted += k[perm[i]]

    return permuted


def shift_left(tab,n):
    for i in range(0, n):
        temp = tab[0]
        for j in range(0, len(tab)):
            if j == len(tab)-1:
                tab[j] = temp
            else:
                tab[j] = tab[j+1]

    return tab


def key_schedule(key):
    permuted_key = permute(key, PC1)

    half_key_l = int(len(permuted_key)) // 2
    left_key = [0] * half_key_l
    right_key = [0] * half_key_l

    # dzieli klucz na dwie polowy - lewa i prawa
    for i in range(half_key_l):
        left_key[i] = int(permuted_key[i])
        right_key[i] = int(permuted_key[half_key_l+i])

    subkeys = []

    for i in range(len(shift_table)):
        new_subkey = ''

        # przesuwa lewy i prawy podklucz o zadaną liczbę z tabeli shift_table z odpowiadającej pozycji
        left_subkey = shift_left(left_key, shift_table[i])
        right_subkey = shift_left(right_key, shift_table[i])

        # łączy uzyskany lewy iprawy podklucz uzyskując podklucz 56 bitowy
        for j in range(len(left_subkey)):
            new_subkey += str(left_subkey[j])

        for j in range(len(left_subkey)):
            new_subkey += str(right_subkey[j])

        # otrzymany klucz 56 bitowy permutuje na nowy podklucz 48 bitowy
        subkeys.append(permute(new_subkey, PC2))

    return subkeys



if __name__ == '__main__':
    print(key_schedule('1010101010111011000010010001100000100111001101101100110011011101') ==
          ['000110010100110011010000011100101101111010001100',
           '010001010110100001011000000110101011110011001110',
           '000001101110110110100100101011001111010110110101',
           '110110100010110100000011001010110110111011100011',
           '011010011010011000101001111111101100100100010011',
           '110000011001010010001110100001110100011101011110',
           '011100001000101011010010110111011011001111000000',
           '001101001111100000100010111100001100011001101101',
           '100001001011101101000100011100111101110011001100',
           '000000100111011001010111000010001011010110111111',
           '011011010101010101100000101011110111110010100101',
           '110000101100000111101001011010100100101111110011',
           '100110011100001100010011100101111100100100011111',
           '001001010001101110001011110001110001011111010000',
           '001100110011000011000101110110011010001101101101',
           '000110000001110001011101011101011100011001101101'])