
def ShiftRows(state):
    result = []

    for i in range(0, len(state)):
        # dodaje pierwszy wiersz bez przesuniecia
        if i == 0:
            result.append(state[0])
        # dodaje reszte wierszy - kazdy koleny przesuwam o 1 więcej niż przedni
        else:
            row = state[i][i:len(state)] + state[i][0:i]
            result.append(row)

    return result

if __name__ == '__main__':
    print(ShiftRows([['5a', '67', '2b', '3a'],
                     ['9e', 'ba', '21', '82'],
                     ['26', 'b5', 'e3', '86'],
                     ['66', '09', '1a', '01']]) ==
                    [['5a', '67', '2b', '3a'],
                     ['ba', '21', '82', '9e'],
                     ['e3', '86', '26', 'b5'],
                     ['01', '66', '09', '1a']])