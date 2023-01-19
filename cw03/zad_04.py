message = '0001001000110100010101101010101111001101000100110010010100110110'

subkeys = ['000110010100110011010000011100101101111010001100',
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
           '000110000001110001011101011101011100011001101101']


def xor(bin_str1, bin_str2):
    bin_xor = ''

    for i in range(len(bin_str1)):
        if bin_str1[i] == bin_str2[i]:
            bin_xor += '0'
        else:
            bin_xor += '1'

    return bin_xor


#Przykładowe funkcje do r_msg_strowania, w przypadku DESa, będzie to funkcja z zdania 4.
def F1(right,subkey):
    return xor(right,subkey[:32])

def F2(right,subkey):
    return 32*'1'


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
        # wykonuje funkcje F dla prawej czesci wiadomosci oraz odpowiedniego klucza
        r_msg_f = F(r_msg_str, subkeys[i])

        #otrzymany wynik z funkcji F xoruje z lewa czescia wiadomosci
        l_xor = xor(r_msg_f, l_msg_str)

        # jesli wykonywany krok nie jest 16, zamieniamy lewa i prawa czesc
        if i < 15:
            l_msg_str = r_msg_str
            r_msg_str = l_xor

    coded_msg = l_xor + r_msg_str

    return coded_msg




if __name__ == '__main__':
    print("Kodowanie:")
    print(Feistel(message,subkeys,F1)=='0101110101010110001010010001100000101111010110001101111110100001')
    print(Feistel(message,subkeys,F2)=='1100110100010011001001010011011000010010001101000101011010101011')

    print("Odkodowanie:")
    print(Feistel(Feistel(message, subkeys, F1), subkeys[::-1], F1) == message)
    print(Feistel(Feistel(message, subkeys, F2), subkeys[::-1], F2) == message)