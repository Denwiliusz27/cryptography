import hashlib


if __name__ == '__main__':
    hash_original = '2d08246bbb3a8f6b0c16b8d8effd2c783233a6a174496731dfff887bb41bc7e7'

    file = open('Campin_Boze_Narodzenie1.png', 'rb')
    obraz1 = file.read()

    file = open('Campin_Boze_Narodzenie2.png', 'rb')
    obraz2 = file.read()

    object1 = hashlib.sha256()
    object1.update(obraz1)

    object2 = hashlib.sha256()
    object2.update(obraz2)

    if object1.hexdigest() == hash_original:
        print("\nPrawdziwy obraz: Campin_Boze_Narodzenie1.png")
    elif object2.hexdigest() == hash_original:
        print("\nPrawdziwy obraz: Campin_Boze_Narodzenie2.png")

    file.close()
