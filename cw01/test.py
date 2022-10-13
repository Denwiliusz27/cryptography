import math
import string

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm',
            'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']

czestotliwosc = {'a':0.0891,'ą':0.0099, 'b':0.0147, 'c':0.0396, 'ć':0.004, 'd':0.0325, 'e':0.0766, 'ę':0.0111, 'f':0.003,
                 'g':0.0142, 'h':0.0108, 'i':0.0821, 'j':0.0228, 'k':0.0351, 'l':0.021, 'ł':0.0182,'m':0.028, 'n':0.0552,
                 'ń':0.002, 'o':0.0775,'ó':0.0085, 'p':0.0313, 'q':0.0014, 'r':0.0469, 's':0.0432,'ś':0.0066, 't':0.0398,
                 'u':0.025, 'v': 0.0004, 'w':0.0465 ,'x':0.0002,'y':0.0376, 'z':0.0564,'ź':0.0006,'ż':0.0083}


liczb_do_lit = dict()
lit_do_liczb = dict()
for i, l in enumerate(alphabet):
    liczb_do_lit[i] = l
    lit_do_liczb[l] = i

def Cezar(tekst, klucz):
    result = ""
    klucz = klucz % len(alphabet)

    for char in tekst:
        isUpper = char.isupper()
        lowerChar = char.lower()

        try:
            index = alphabet.index(lowerChar)
        except:
            result += char
            continue

        index = (index + klucz) % len(alphabet)
        if (index < 0):
            index = len(alphabet) - index - 1

        newChar = alphabet[index]
        if (isUpper):
            newChar = newChar.upper()

        result += newChar

    return result




def SquareRootErrorDict(base, sub):
    error = 0
    for key in base.keys():
        a = base.get(key, 0)
        b = sub.get(key, 0)
        error += math.sqrt((a - b) * (a - b))
    if len(base) > 0:
        error /= len(base)
    return error


def CountFreq(text):
    freq = {}
    charCount = 0
    for char in text:
        if char not in alphabet:
            continue

        freq[char] = freq.get(char, 0) + 1
        charCount += 1
    if charCount == 0:
        return freq

    for key in freq:
        freq[key] /= charCount
    return freq


def BestCezar(text):
    resultList = []

    for i in range(len(alphabet)):
        cezar = Cezar(text, i)
        freq = CountFreq(cezar)
        error = SquareRootErrorDict(czestotliwosc, freq)
        resultList.append((i, error))
        print('For ', i, ', sqError: ', error)

    resultList.sort(key=lambda entry: entry[1])
    return resultList



def Vignere_zaszyfruj(tekst, klucz):
    result = ""
    keyCounter = 0

    for char in tekst:
        isUpper = char.isupper()
        lowerChar = char.lower()

        if lowerChar not in lit_do_liczb:
            result += char
            continue

        key = klucz[keyCounter % len(klucz)].lower()
        offset = lit_do_liczb[lowerChar] + lit_do_liczb[key]
        offset = offset % len(alphabet)
        keyCounter += 1

        newChar = liczb_do_lit[offset]
        if (isUpper):
            newChar = newChar.upper()

        result += newChar

    return result


def Vignere_odszyfruj(tekst, klucz):
    result = ""
    keyCounter = 0

    for char in tekst:
        isUpper = char.isupper()
        lowerChar = char.lower()

        if lowerChar not in lit_do_liczb:
            result += char
            continue

        key = klucz[keyCounter % len(klucz)].lower()
        offset = lit_do_liczb[lowerChar] - lit_do_liczb[key]
        if offset < 0:
            offset = -offset
            offset = len(liczb_do_lit) - offset
        keyCounter += 1

        newChar = liczb_do_lit[offset]
        if (isUpper):
            newChar = newChar.upper()

        result += newChar

    return result


if __name__ == '__main__':
    plik=open('ksiazka2.txt', encoding='utf8')
    ksiazka=plik.read()
    plik.close()

    remove_white_dict = dict.fromkeys(map(ord, string.whitespace))
    remove_punct_dict = dict.fromkeys(map(ord, string.punctuation))
    remove_digits_dict = dict.fromkeys(map(ord, string.digits))
    text = ksiazka
    text = text.translate(remove_white_dict)
    text = text.translate(remove_punct_dict)
    text = text.translate(remove_digits_dict)
    # text = text[0:50]

    print(len(text))

    # N disvovery

    guessedLengths = []
    terminalLength = min(len(text), 10)
    for n in range(1, terminalLength):
        print("N: ", n)
        filteredN = text[1::n]
        bestCezar = BestCezar(filteredN)
        guessedLengths.append((n, bestCezar[0][1]))

    guessedLengths.sort(key=lambda entry: entry[1])
    print('Password length is probably ', guessedLengths[0][0])

    # Password decoding
    pswdLen = guessedLengths[0][0]

    key = ""
    for n in range(0, pswdLen):
        bestCezar = BestCezar(text[n::pswdLen])
        key += liczb_do_lit[35 - bestCezar[0][0]]