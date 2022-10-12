import matplotlib.pyplot as plt
import numpy as np
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

book_frequency = {'a': 0, 'ą': 0, 'b': 0, 'c': 0, 'ć': 0, 'd': 0, 'e': 0, 'ę': 0, 'f': 0,
                  'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'ł': 0, 'm': 0, 'n': 0,
                  'ń': 0, 'o': 0, 'ó': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 'ś': 0, 't': 0,
                  'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'ź': 0, 'ż': 0}


def analize(text):
    amount = 0

    for char in text:
        if char in string.punctuation or char in string.whitespace or char in string.digits:
            continue
        elif char.isupper():
            char = char.lower()

        book_frequency[char] += 1
        amount += 1

    for key in book_frequency:
        book_frequency[key] = book_frequency[key] / amount

    plt.bar(book_frequency.keys(), book_frequency.values())
    plt.show()


def Cezar(text, key):
    is_upper = False
    final = ''

    for character in text:
        if character in string.punctuation or character in string.whitespace or character in string.digits:
            final += character
            continue
        elif character.isupper():
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

    return final


if __name__ == '__main__':
    file = open('ksiazka1.txt', encoding='utf8')
    book = file.read()
    file.close()
    analize(book)

    print('Input key value: ')
    key = int(input())

    output_file = open('ksiazka1_output.txt', 'a')
    output_file.write(Cezar(book, -key))
    output_file.close()

    print('Fin')
