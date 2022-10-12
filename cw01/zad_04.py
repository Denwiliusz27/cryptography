import string

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
            'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']


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
            position = lit_do_liczb[char]  # alphabet.index(char)
            shift = lit_do_liczb[key[i % len(key)]]

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
