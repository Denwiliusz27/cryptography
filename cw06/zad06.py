def padding(msg, L):
    # obliczam różnice
    difference = L - len(msg)
    result = msg

    # jeśli różnica jest wartością dodatnią
    if difference > 0:
        # to do msg dodaje tą wartość zapisaną szesnastkowo tyle razy ile ona wynosi
        for i in range(difference):
            result.append('0' + str(difference))
    # jeśli różnica jest 0
    elif difference == 0:
        # dodaję do msg L razy wartość równą L zapisaną szesnastkowo
        for i in range(L):
            result.append('0' + str(L))
    # jesli różnica jest mniejsza od zera
    else:
        new_l = L
        i = 2
        #  obliczam nowe L będace wielokrotnością wejściowego L do czasu aż nowe L będzie większe od wejściowego L
        while new_l < len(msg):
            new_l *= i

        # rekurencyjnie wykonuje funkcje dla nowego L
        result = padding(msg, new_l)

    return result


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


if __name__ == '__main__':
    print(oracle(['ed', 'd2', '76', 'dc', '2b', 'd6', 'ff', 'a6', '35', '35', 'be', '1a', '26', '03', '03', '03'],
                 16) == True)
    print(oracle(['54', '10', '38', 'c0', 'cc', 'e7', '8d', '8f', '70', '22', 'aa', '06', '06', '06', '06', '06'],
                 16) == False)
    print(oracle(
        ['8e', 'ba', 'e3', 'd9', '76', '08', 'f1', 'd2', 'ca', '09', '39', '6b', 'b0', '4d', '36', '94', '49', '69',
         '30', '57', '3e', '9d', 'df', 'd7', 'fa', 'aa', '95', '5c', '60', '5f', '02', '02'], 16) == True)
    print(oracle(['1e', '17', '53', '04', '04', '04', '04', '04'], 8) == True)
    print(oracle(['1e', '17', '53', '04', '04', '04', '04', '00'], 8) == False)
    print(oracle(['1e', '17', '53', '04', '04', '04', '04', 'aa'], 8) == False)
    print(oracle(['42', 'f2', '07', 'c7', '32', 'd8', '10', '7e', 'a5', '53', '0d', '18', '04', '04', '04', '04'],
                 8) == True)
    print(oracle(['42', 'f2', '07', 'c7', '32', 'd8', '10', '7e', 'a5', '53', '0d', '18', '04', '00', '04', '04'],
                 8) == False)
    print(oracle(['1e', '17', '53', '69', '01', 'r2', 'ff', '1g', '08', '08', '08', '08', '08', '08', '08', '08'],
                 8) == True)