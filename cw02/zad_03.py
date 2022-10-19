from PIL import Image
import numpy


def add_pic(img, key):
    a_img = numpy.array(img, dtype=numpy.uint8)
    a_key = numpy.array(key, dtype=numpy.uint8)

    result = numpy.random.randint(1, size=(heigh, width), dtype=numpy.uint8)

    for i in range(0, len(a_img)):
        for j in range(0, len(a_img[0])):
            a = a_img[i][j]
            k = a_key[i][j]
            if a == k:
                result[i][j] = 0
            else:
                result[i][j] = 255

    return result


if __name__ == '__main__':
    miki = Image.open('miki.png').convert('L')
    quest = Image.open('quest.png').convert('L')

    width, heigh = miki.size

    key = numpy.random.randint(0, 2, size=(heigh, width), dtype=numpy.uint8)

    for i in range(0, heigh):
        for j in range(0, width):
            if key[i][j] == 1:
                key[i][j] = 255

    key_img = Image.fromarray(key)
    key_img.save("key_img.png", "PNG")

    miki_coded = add_pic(miki, key)
    miki_coded_img = Image.fromarray(miki_coded)
    miki_coded_img.save("miki_coded.png", "PNG")

    quest_coded = add_pic(quest, key)
    quest_coded_img = Image.fromarray(quest_coded)
    quest_coded_img.save("quest_coded.png", "PNG")

    final_coded = add_pic(quest, miki)
    final_coded_img = Image.fromarray(final_coded)
    final_coded_img.save("final.png", "PNG")
