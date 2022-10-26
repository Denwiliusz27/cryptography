def find_word(msg_sum, word):
    word_b = [0] * len(word)

    for i in range(0, len(word)):
        word_b[i] = ord(word[i])

    for i in range(0, len(msg_sum) - len(word_b)):
        msg_with_key = msg_sum.copy()
        j = 0

        while j < len(word_b):
            msg_with_key[i + j] = msg_sum[i + j] ^ word_b[j]
            j += 1

        for a in range(i, len(word_b) + i):
            msg_with_key[a] = chr(msg_with_key[a])

        print('Word on pos = ', i, ': ', msg_with_key[i:i + len(word_b)])


def add_str(msg1, msg2):
    msg_sum = [''] * len(msg1)
    msg1_b = [0] * len(msg1)
    msg2_b = [0] * len(msg2)

    for i in range(0, len(msg1)):
        msg1_b[i] = ord(msg1[i])
        msg2_b[i] = ord(msg2[i])
        msg_sum[i] = chr(msg1_b[i] ^ msg2_b[i])

    return msg_sum


def add_str_to_message_on_index(msg, index, str):
    j = 0

    for i in range(index, index + len(str)):
        msg[i] = str[j]
        j += 1

    print("msg: ", msg)

    return msg


if __name__ == '__main__':
    msg1_enc = '\x1e\x17\x0c\x12\x1b\x08\x0cf\x0e\x11x\x1a\x1c\x12o\x06\x18\x1f\x17\x03\x10\x01fkh\x1f\x08'
    msg2_enc = '\x0b\ni\x07\x1c\x02k\x1f\x16e\x01\x0b\x07\x03\n\x15\x15\x0c\x1el\x07\x03\x03\x16\x01\x01\x02'

    message_sum = add_str(msg1_enc, msg2_enc)
    print(message_sum)

    msg1_encoded = [''] * len(msg1_enc)
    msg2_encoded = [''] * len(msg1_enc)

    msg1_final = ''
    msg2_final = ''

    j = 0
    while (1):
        print('\n Enter possible word: ')
        key = input()

        if key == '-1':
            break

        for i in range(0, len(message_sum) - len(key) + 1):
            encoded_str = add_str(message_sum[i:i + len(key)], key)
            print('i = ', i, ': ', encoded_str)

        print('\n Enter index nr: ')
        index = int(input())

        if index == -1:

            break

        encoded_str = add_str(message_sum[index:index + len(key)], key)
        print('index = ', index, ': ', encoded_str)

        if j % 2 == 0:
            add_str_to_message_on_index(msg1_encoded, index, key)
            add_str_to_message_on_index(msg2_encoded, index, encoded_str)
        else:
            add_str_to_message_on_index(msg1_encoded, index, encoded_str)
            add_str_to_message_on_index(msg2_encoded, index, key)

        j += 1

    for n in range(0, len(msg1_encoded)):
        msg1_final = msg1_final + msg1_encoded[n]
        msg2_final = msg2_final + msg2_encoded[n]

    print("Message 1: ", msg1_final)
    print("Message 2: ", msg2_final)