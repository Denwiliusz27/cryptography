import numpy as np
from PIL import Image


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


def shift_left(tab,n):
    for i in range(0, n):
        temp = tab[0]
        for j in range(0, len(tab)):
            if j == len(tab)-1:
                tab[j] = temp
            else:
                tab[j] = tab[j+1]

    return tab



if __name__ == '__main__':
    print("\nBinary to decimal:")
    print(bin2dec('0') == 0)
    print(bin2dec('10') == 2)
    print(bin2dec('111') == 7)
    print(bin2dec('1001') == 9)
    print(bin2dec('0001') == 1)

    print("\nDecimal to binary:")
    print(dec2bin(0, 1) == '0')
    print(dec2bin(2, 2) == '10')
    print(dec2bin(7, 4) == '0111')
    print(dec2bin(9, 4) == '1001')
    print(dec2bin(1, 4) == '0001')

    print("\nShift table: ")
    print(shift_left([1, 2, 3, 4], 2) == [3, 4, 1, 2])
    print(shift_left([1, 2, 3, 4], 3) == [4, 1, 2, 3])
    print(shift_left([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2])
