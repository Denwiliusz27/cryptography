import numpy as np
import textwrap

hex_to_bin = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111' }

bin_to_hex = { '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
                '1000':'8', '1001':'9', '1010':'a', '1011':'b', '1100':'c', '1101':'d', '1110':'e', '1111':'f' }


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


def prepare_state(msg):
    div_msg = textwrap.wrap(msg, 8)
    matrix = []
    row = []

    for i in range(len(div_msg)):
        if i%4 == 0 and i != 0:
            matrix.append(row)
            row = []

        msg = div_msg[i]
        msg1 = msg[0:int(len(msg)/2)]
        msg2 = msg[int(len(msg)/2):len(msg)]

        b = bin_to_hex[msg1] + bin_to_hex[msg2]
        row.append(b)

    matrix.append(row)
    return matrix


if __name__ == '__main__':
    print("Hex to binary:")
    print(hex2bin('a', 2) == '1010')
    print(hex2bin('a', 5) == '01010')
    print(hex2bin('1a', 2) == '11010')
    print(hex2bin('1a', 7) == '0011010')

    print("Prepare state:")
    msg = '01000110000010100000101110100010110111111100000001111011000100010010001111010010010011011101110011010011010000000100001100001001'
    print(prepare_state(msg) ==
          [['46', '0a', '0b', 'a2'],
           ['df', 'c0', '7b', '11'],
           ['23', 'd2', '4d', 'dc'],
           ['d3', '40', '43', '09']])