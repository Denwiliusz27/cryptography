hex_to_bin = { '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111' }

SBox=[['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
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


def bin2dec(bin_str):
    dec_val = 0

    for i in range(0, len(bin_str)):
        if bin_str[i] == '1' :
            dec_val += 2**(len(bin_str)-i-1)

    return dec_val


def SubBytes(state):
    # pobieram ilosc kolumn i wierszy state
    rows = len(state)
    columns = len(state[0])

    # tworze tabele wynikową z odpowiednia iloscia wierszy i kolumn
    result = [['' for x in range(rows)] for y in range(columns)]

    for i in range(rows):
        for j in range(columns):
            # pobieram pierwszy znak odczytanego ciagu
            first = state[i][j][0]
            #pobieram drugi element odczytanego ciagu
            last = state[i][j][1]

            # pierwszy element zamieniam na odpowiadajaca mu wartosc w syst. dziesietnym = nr wiersza
            row = bin2dec(hex_to_bin[first])
            # drugi element zamieniam na odpowiadajaca mu wartosc w syst. dziesietnym = nr kolumny
            col = bin2dec(hex_to_bin[last])

            result[i][j] = SBox[row][col]

    return result


if __name__ == '__main__':
    print(SubBytes([['46', '0a', '0b', 'a2'],
                    ['df', 'c0', '7b', '11'],
                    ['23', 'd2', '4d', 'dc'],
                    ['d3', '40', '43', '09']]) ==
                   [['5a', '67', '2b', '3a'],
                    ['9e', 'ba', '21', '82'],
                    ['26', 'b5', 'e3', '86'],
                    ['66', '09', '1a', '01']])