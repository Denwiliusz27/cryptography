hexadecimal = { '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
                '1000':'8', '1001':'9', '1010':'a', '1011':'b', '1100':'c', '1101':'d', '1110':'e', '1111':'f' }


def add_GF(p,q):
    sum = ''

    if len(p) > len(q):
        b_len = len(p)
    else:
        b_len = len(q)

    # dopełniam oba ciągi zerami, aby kazdy miał po tyle samo znakow
    p = p.zfill(b_len)
    q = q.zfill(b_len)

    for i in range(b_len):
        if p[i] == q[i]:
            sum += '0'
        else:
            sum += '1'

    # pozbywam sie wiodących zer
    sum = sum.lstrip('0')
    return sum


def bin2hex(bin_str, pad):
    # dopisuję 0 na początku, aby długość tekstu miała ilość znaków podzielną na 4
    if len(bin_str)%4 == 1:
        bin_str = '000' + bin_str
    elif len(bin_str)%4 == 2:
        bin_str = '00' + bin_str
    elif len(bin_str)%4 == 3:
        bin_str = '0' + bin_str

    hex = ''

    i = len(bin_str)

    # biorę kolejne 4 znaki idąc od prawej strony i zamianiam na znak ze słownika
    while i > 1:
        hex_p = hexadecimal[bin_str[i-4:i]]
        hex = hex_p + hex
        i -= 4

    # dopełniam do wymaganej liczby znaków
    hex = hex.zfill(pad)

    return hex


if __name__ == '__main__':
    print(add_GF('110', '11') == '101')
    print(add_GF('110', '101') == '11')

    print(bin2hex('1101', 2) == '0d')
    print(bin2hex('11010011', 2) == 'd3')
    print(bin2hex('1111111', 3) == '07f')
    print(bin2hex('1', 1) == '1')
