import matplotlib.pyplot as plt
import math
import string

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
            'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']

frequency = {'a': 0.0891, 'ą': 0.0099, 'b': 0.0147, 'c': 0.0396, 'ć': 0.004, 'd': 0.0325, 'e': 0.0766, 'ę': 0.0111,
             'f': 0.003,
             'g': 0.0142, 'h': 0.0108, 'i': 0.0821, 'j': 0.0228, 'k': 0.0351, 'l': 0.021, 'ł': 0.0182, 'm': 0.028,
             'n': 0.0552,
             'ń': 0.002, 'o': 0.0775, 'ó': 0.0085, 'p': 0.0313, 'q': 0.0014, 'r': 0.0469, 's': 0.0432, 'ś': 0.0066,
             't': 0.0398,
             'u': 0.025, 'v': 0.0004, 'w': 0.0465, 'x': 0.0002, 'y': 0.0376, 'z': 0.0564, 'ź': 0.0006, 'ż': 0.0083}

# przechowuje częstotliwość znaków w podanym tekście
book_frequency = {'a': 0, 'ą': 0, 'b': 0, 'c': 0, 'ć': 0, 'd': 0, 'e': 0, 'ę': 0, 'f': 0,
                  'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'ł': 0, 'm': 0, 'n': 0,
                  'ń': 0, 'o': 0, 'ó': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'ś': 0, 't': 0,
                  'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'ź': 0, 'ż': 0}


def cezar(text, key):
    is_upper = False
    final = ''

    for character in text:
        if character.isupper():
            character = character.lower()
            is_upper = True

        if character in alphabet:
            position = alphabet.index(character)

            if position + key >= len(alphabet):
                temp = alphabet[abs(len(alphabet) - (position + key))]
            else:
                temp = alphabet[position + key]

            if is_upper:
                final += temp.upper()
                is_upper = False
            else:
                final += temp
        else:
            final += character
            continue

    return final


# porównuje otrzymane średnie od bazowych
def check_error(base, test):
    error = 0

    for key in base.keys():
        k1 = base.get(key, 0)
        k2 = test.get(key, 0)
        error += math.sqrt((k1 - k2) * (k1 - k2))

    return error / len(base)


# zwraca słownik z wynikami o najmniejszej różnicy wobec bazowych wartości
def find_best_cezar(text):
    result = []

    # wykonuje cezara dla podanego tekstu i dla kluczy o różnych długościach
    for key in range(len(alphabet)):
        cezar_txt = cezar(text, key)
        cezar_frequency = set_frequency(cezar_txt)  # ustawia częstotliwość w słowniku po wykonaniu cezara
        error = check_error(frequency,
                            cezar_frequency)  # porównuje otrzymany słownik z bazowym i wstawia wynik do tabeli
        result.append((key, error))
        # print('Key: ', key, ", error: ", error)

    result.sort(key=lambda entry: entry[1])  # wybiera dł klucza dla której błąd był najmniejszy
    return result


def find_key(text):
    test_lengths = []

    # znajduje prawdopodobna dl klucza poprzez wykonywanie cezara na tekscie co n-ty znak
    for n in range(1, 10):
        print('_____________________________')
        print('sprawdzam klucz o odl = ', n)
        new_text = text[1::n]  # z tekstu tworzy tekst z co n-tej litery
        best = find_best_cezar(new_text)  # wykonuje cezara na nowo powstałym tekście
        test_lengths.append((n, best[0][1]))  # dodaje klucz razem z wartością błędu dla niego

    test_lengths.sort(key=lambda entry: entry[1])  # wybiera dl klucza dla której różnica była najmniejsza
    print('Prawdopodobna dl klucza = ', test_lengths[0][0])

    decoding_key = test_lengths[0][0]
    new_key = ''

    for n in range(0, decoding_key):
        # znajduje najlepszego cezara w tekście co n-ty znak, przesuwa o jeden znak przy każdej pętli
        best_c = find_best_cezar(text[n::decoding_key])  # zwraca wartosc przesuniecia
        new_key += liczb_do_lit[35 - best_c[0][0]]
        print('key: ', new_key)

    return new_key


# funkcja zliczająca wystąpienia kolejnych znaków w czytanym tekście
def set_frequency(text):
    amount = 0
    freq = {}

    for char in text:
        if char not in alphabet:
            continue

        freq[char] = freq.get(char, 0) + 1
        amount += 1

    if amount == 0:
        return freq

    for key in freq:
        freq[key] = freq[key] / amount

    return freq


def Vignere_encrypt(text, key):
    is_upper = False
    final = ''
    i = 0

    for char in text:
        if char in string.punctuation or char in string.whitespace or char in string.digits:
            final += char
            continue
        elif char.isupper():
            char = char.lower()
            is_upper = True

        if char in alphabet:
            # pobierany jest nr pozycji w alfabecie czytanego znaku
            position = lit_do_liczb[char]  # alphabet.index(char)

            # wyliczane jest przesunięcie, jako nr pozycji w alfabecie znaku z klucza
            shift = lit_do_liczb[key[i % len(key)]]

            # pobranie z alfabetu znaku z pozycji będącej sumą position + shift
            if position + shift >= len(liczb_do_lit):
                temp = liczb_do_lit[abs(len(liczb_do_lit) - (position + shift))]
            else:
                temp = liczb_do_lit[position + shift]

            if is_upper:
                final += temp.upper()
                is_upper = False
            else:
                final += temp
        i += 1

    return final


def Vignere_decrypt(text, key):
    final = ''

    # klucz zostaje odwrócony
    for char in key:
        final += liczb_do_lit[(len(alphabet) - lit_do_liczb[char]) % len(alphabet)]

    # wywołanie funkcji szyfrującej z odwróconym kluczem
    return Vignere_encrypt(text, final)


if __name__ == '__main__':
    liczb_do_lit = dict()
    lit_do_liczb = dict()
    for i, l in enumerate(alphabet):
        liczb_do_lit[i] = l
        lit_do_liczb[l] = i

    file = open('ksiazka2.txt', encoding='utf8')
    book = file.read()
    file.close()

    # usuwam kropki, przecinki, spacje, cyfry z tekstu
    test_text = book.translate(str.maketrans('', '', string.whitespace))
    test_text = test_text.translate(str.maketrans('', '', string.punctuation))
    test_text = test_text.translate(str.maketrans('', '', string.digits))
    print(len(test_text))

    new_key = find_key(test_text)

    output_file = open('ksiazka2_output.txt', 'a')
    final_txt = Vignere_decrypt(book, new_key)
    output_file.write(final_txt)
    output_file.close()
