#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

alfabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
           'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']


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

        if character in alfabet:
            position = alfabet.index(character)

            if position + key > len(alfabet):
                temp = alfabet[abs(len(alfabet) - (position + key))]
            else:
                temp = alfabet[position + key]

            if is_upper:
                final += temp.upper()
                is_upper = False
            else:
                final += temp

    return final


if __name__ == '__main__':
    print(Cezar('Ala ma kota.', 3)  == 'Cnc oc mqwc.')
    print(Cezar('Ala ma kota.', 20)  == 'Óżó ąó źćió.')
    print(Cezar('Ala ma 2 koty.', 5)  == 'Dod pd 2 ńsyą.')
    print(Cezar(
        'Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.',
        7)
          == 'Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.')
    print(Cezar('Cnc oc mqwc.', -3) == 'Ala ma kota.')
    print(Cezar('Óżó ąó źćió.', -20) == 'Ala ma kota.')
    print(Cezar('Dod pd 2 ńsyą.', -5) == 'Ala ma 2 koty.')
    print(Cezar(
        'Jęxkrsk eępk, vxuesc źxżj,\nGkćyńpsk ćqtxćkhćksńę!\nVxćkecźchn óyćźęqźuą eęjks hżj\nSńk ąxuhń jt ńyźsńksńę.',
        -7)
          == 'Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.')
