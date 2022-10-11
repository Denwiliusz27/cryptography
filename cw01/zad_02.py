#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

alfabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
           'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']


# funkcja odszyfrowująca podany tekst za pomoca podanego klucza
def decrypt(text):
    is_upper = False
    key = 0

    while key > -35:
        key -= 1
        final = ''

        for char in text:
            if char in string.punctuation or char in string.whitespace or char in string.digits:
                final += char
                continue
            elif char.isupper():
                char = char.lower()
                is_upper = True

            if char in alfabet:
                position = alfabet.index(char)

                if position + key >= len(alfabet):
                    temp = alfabet[abs(len(alfabet) - (position + key))]
                else:
                    temp = alfabet[position + key]

                if is_upper:
                    final += temp.upper()
                    is_upper = False
                else:
                    final += temp

        print("key: ", -key, " - ", final)



if __name__ == '__main__':
    tekst = 'Hćcrek okyź hćęy? Okzpń sńóź rsńk t źt sńk vcźę, ąńkr. Okzpń vcźęofhkrż żyńqżol ącźqżręhćci, sńk ąńkr.'
    decrypt(tekst)
