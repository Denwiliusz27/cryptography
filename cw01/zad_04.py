import string

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
            'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']


# funkcja szyfrująca dla szyfru Vignere'a
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


# funkcja odszyfrowująca szyfr Vignere
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

    print(Vignere_encrypt('Ala ma kota.', 'ela') == 'Eva ql kśda.')
    print(Vignere_encrypt('Ala ma kota.', 'tygrys') == 'Thg ćy bhqg.')
    print(Vignere_encrypt('Ala ma 2 koty.', 'indywidualistyczny') == 'Iyd jw 2 ssńy.')
    print(Vignere_encrypt(
        'Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.',
        'asnyk')
          == 'Dsdbwnx myue, hdmjnó fodd,\nTrvbicżb hłfdvocprksa!\nHdvożófumh bevćaćfmę żsqbx cmq\nKse ńdmmi wą ębtevbxis.')

    print('========================================')

    print(Vignere_decrypt('Eva ql kśda.', 'ela') == 'Ala ma kota.')
    print(Vignere_decrypt('Thg ćy bhqg.', 'tygrys') == 'Ala ma kota.')
    print(Vignere_decrypt('Iyd jw 2 ssńy.', 'indywidualistyczny') == 'Ala ma 2 koty.')
    print(Vignere_decrypt(
        'Dsdbwnx myue, hdmjnó fodd,\nTrvbicżb hłfdvocprksa!\nHdvożófumh bevćaćfmę żsqbx cmq\nKse ńdmmi wą ębtevbxis.',
        'asnyk')
          == 'Daremne żale, próżny trud,\nBezsilne złorzeczenia!\nPrzeżytych kształtów żaden cud\nNie wróci do istnienia.')
