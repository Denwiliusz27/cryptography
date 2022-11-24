import textwrap

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}

IP = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61,
      53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7, 56, 48,
      40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44,
      36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6]

FP = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37,
      5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3,
      43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41,
      9, 49, 17, 57, 25, 32, 0, 40, 8, 48, 16, 56, 24]

PC1 = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58,
       50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12,
       4, 27, 19, 11, 3]

shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3,
       25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39,
       50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

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
        if bin_str[i] == '1':
            dec_val += 2 ** (len(bin_str) - i - 1)

    return dec_val


def F(right, subkey):
    # permutacja E
    right_e = permute(right, E)

    # xor wyniku permuacji oraz klucza
    right_xor = xor(right_e, subkey)

    # podział otrzymanego ciągu na 8 podciagów po 6 elementów
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


def Feistel(message, subkeys, F):
    half_msg_len = int(len(message)) // 2
    l_msg = [''] * half_msg_len
    r_msg = [''] * half_msg_len

    # dzieli wiadomosc na dwie polowy - lewa i prawa
    for i in range(half_msg_len):
        l_msg[i] = message[i]
        r_msg[i] = message[half_msg_len + i]

    l_msg_str = ''.join(l_msg)
    r_msg_str = ''.join(r_msg)

    for i in range(0, 16):
        # wykonuje wunkcje F dla prawej czesci wiadomosci oraz odpowiedniego klucza
        r_msg_f = F(r_msg_str, subkeys[i])

        # otrzymany wynik z funkcji F xorje z lewa czescia wiadomosci
        l_xor = xor(r_msg_f, l_msg_str)

        # jesli wykonywany krok nie jest 16, zamieniamy lewa i prawa czesc
        if i < 15:
            l_msg_str = r_msg_str
            r_msg_str = l_xor

    coded_msg = l_xor + r_msg_str

    return coded_msg


def shift_left(tab, n):
    for i in range(0, n):
        temp = tab[0]
        for j in range(0, len(tab)):
            if j == len(tab) - 1:
                tab[j] = temp
            else:
                tab[j] = tab[j + 1]

    return tab


def key_schedule(key):
    permuted_key = permute(key, PC1)

    half_key_l = int(len(permuted_key)) // 2
    left_key = [0] * half_key_l
    right_key = [0] * half_key_l

    # dzieli klucz na dwie polowy - lewa i prawa
    for i in range(half_key_l):
        left_key[i] = int(permuted_key[i])
        right_key[i] = int(permuted_key[half_key_l + i])

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


def DES(message, subkeys):
    message_ip = permute(message, IP)
    feistel = Feistel(message_ip, subkeys, F)
    message_fp = permute(feistel, FP)

    return message_fp


def dec2bin(dec_str, pad):
    return format(int(dec_str), '0' + str(pad) + 'b')


def split_img(img_bin, n):
    img_split = []
    for i in range(0, len(img_bin), n):
        img_split.append(img_bin[i:i + n])
    return img_split


def CBCde(msg, key, iv):
    result = []

    # tworze liste podkluczy
    subkeys = key_schedule(key)
    # dziele wiadomosc na czesci po 64 bity
    sub_msg = textwrap.wrap(msg, 64)

    vector = iv

    for i in range(len(sub_msg)):
        # odpowiednia czesc wiadomosci przepuszczam przez DES'a wraz z lista podkluczy.
        new_msg = DES(sub_msg[i], subkeys[::-1])
        # otrzymany ciag xor'uje z vektorem i dodaje do tablicy wynikowej
        result.append(xor(vector, new_msg))
        # vector dla kolejnego przebiegu petli ustawiam jako poprzedzajaca czesc wiadomosci
        vector = sub_msg[i]

    final = ''.join(result)
    return final


def oracle(msg, L):
    # sprawdzam czy ostatni element nie jest ciągiem znaków, dwoma zerami, lub jego wartość nie jest większa od L
    if (not msg[len(msg) - 1].isnumeric()) or (msg[len(msg) - 1] == '00') or \
            (int(msg[len(msg) - 1]) > L) or (len(msg) % L != 0) or (len(msg) == 0):
        return False

    # pobieram ostatni element
    padding_el = msg[len(msg)-1]

    if (len(msg) < int(padding_el)):
        return False

    # sprawdzam ostatnie n elementów tablicy, gdzie n - wartość ostatniego elementu
    for i in range(len(msg)-2, len(msg)-1-int(padding_el), -1):
        # jeśli i-ty element jest różny od ostatniego elem, tablicy
        # print("sprawdzam: ", msg[i])
        if msg[i] != padding_el:
            return False

    return True


#######################################################################################################################

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


def dec2hex(dec, pad):
    val = hex(dec)[2:]
    return val.rjust(pad, '0')


def msghex_to_msgbin(msg):
    return ''.join([format(int(i, 16), '08b') for i in msg])


def msgbin_to_msghex(msg):
    return [format(int(a, 2), '02x') for a in [msg[8 * i:8 * i + 8] for i in range(8)]]


def server(msg_enc, iv):
    key = '0111101000001010110010000001010101111111100000000000101000110001'
    msg = CBCde(msghex_to_msgbin(msg_enc), key, msghex_to_msgbin(iv))
    return oracle(msgbin_to_msghex(msg), 8)


def find_padding_index(msg_ec, iv):
    for i in range(len(msg_enc)):
        new_iv = iv.copy()
        new_iv[i] = 'aa'

        if(server(msg_ec, new_iv) == False):
            return i
    return 0


def padding_oracle(msg_enc, iv):
    # sprawdzam index od którego zaczyna sie padding
    padding_value = find_padding_index(msg_enc, iv)
    msg_len = len(msg_enc)

    # tworze nowa wiadomosc z wartosciami paddingu
    new_iv = ['00' for i in range(msg_len)]
    for i in range(msg_len):
        if i >= padding_value:
            new_iv[i] = '0' + str(msg_len-padding_value)

    suspected = iv.copy()

    # ustawiam padding jako dł tablicy - wartość paddingu
    padding_value = msg_len-padding_value

    for j in range(msg_len-padding_value):
        # tworze element 0+padding_value+1
        new_padd_el = '0' + str(msg_len-padding_value+j-1)

        # modyfikuje padding_val+1 ostatnich bajtów aby wartość była o 1 wększa
        for i in range(1, padding_value+j+1):
            suspected[msg_len-i] = bin2hex(xor(xor(hex2bin(iv[msg_len-i], 8), hex2bin(new_iv[msg_len-i], 8)), hex2bin(new_padd_el, 8)), 2)

        # szukam nowego bajtu wiadomości za pomocą wyroczni
        new_val = suspected[padding_value+1-j]
        for i in range(255):
            suspected[padding_value+1-j] = dec2hex(i, 2)
            if (server(msg_enc, suspected)):
                break

        # wstawiam nową wartość po xorowaniu to wyniku
        index = '0' + str(padding_value+1+j)
        new_iv[padding_value+1-j] = bin2hex( xor( xor(hex2bin(suspected[padding_value+1-j], 8), hex2bin(index, 8)), hex2bin(new_val, 8)), 2)

    return new_iv


if __name__ == '__main__':
    msg_enc = ['be', '21', 'a2', 'd7', '9d', 'c7', '8d', 'a3']
    iv = ['36', '92', '8b', '53', 'ef', 'f2', '7a', 'e4']

    print("Message: ", padding_oracle(msg_enc, iv))