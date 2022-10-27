
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


if __name__ == '__main__':
    print("Permute:")
    print(permute('abcd', [1, 0, 2, 3]) == 'bacd')
    print(permute('abcd', [3, 2, 1, 0]) == 'dcba')
    print(permute('abcd', [0, 1, 2, 3, 0]) == 'abcda')
    print(permute('1100', [0, 1, 3, 2, 0, 3]) == '110010')
    print(permute('1100', [0, 2, 1]) == '101')

    print("\nXOR:")
    print(xor('0', '0') == '0')
    print(xor('1', '1') == '0')
    print(xor('01', '11') == '10')
    print(xor('1101', '1111') == '0010')
    print(xor('11111', '11111') == '00000')
    print(xor('11111', '11111') == '00000')