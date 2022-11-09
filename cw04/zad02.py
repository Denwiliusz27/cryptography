def add_GF(p,q):
    sum = ''

    if len(p) > len(q):
        b_len = len(p)
    else:
        b_len = len(q)

    # dopełniam oba ciągi zerami, aby kazdy miał po 3 znaki
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


def multiply(p,q):
    multiplication_el = []
    n = 0

    # biore druga liczbe, przechodze od konca i mnoze - jesli elem = 1 - dodaje p z odpowiednia iloscia zer do tabeli,
    # jesli 0 - dodaje same zera
    for i in reversed(q):
        if i == '1':
            multiplication_el.append(p + n *'0')
        else:
            multiplication_el.append(len(p) * '0')
        n += 1

    sum = ''

    # dodaje elementy z tabeli do siebie i otrzymuje wynik koncowy
    if len(multiplication_el) > 1:
        sum = add_GF(multiplication_el[0], multiplication_el[1])

        if len(multiplication_el) > 2:
            for i in range(2, len(multiplication_el)):
                sum = add_GF(sum, multiplication_el[i])
    else:
        sum = multiplication_el[0]

    return sum



if __name__ == '__main__':
    print(multiply('10', '1') == '10')
    print(multiply('10', '10') == '100')
    print(multiply('110', '11') == '1010')
    print(multiply('11', '110') == '1010')