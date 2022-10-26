import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


def add_str(msg1, msg2):
    msg_sum = [''] * len(msg1)
    msg1_b = [0] * len(msg1)
    msg2_b = [0] * len(msg2)

    for i in range(0, len(msg1)):
        msg1_b[i] = ord(msg1[i])
        msg2_b[i] = ord(msg2[i])
        msg_sum[i] = chr(msg1_b[i] ^ msg2_b[i])

    return msg_sum


def calc_zeros_perc(msg):
    z_cout = 0

    for i in range(0, len(msg)):
        if ord(msg[i]) == 0:
            z_cout += 1

    return z_cout


if __name__ == '__main__':
    messages = []
    zeros_for_couple = np.zeros((10, 10))

    for i in range(0, 10):
        msg = open("msg" + str(i) + ".txt", "r")
        messages.append(msg.read())
        msg.close()

    for i in range(0, len(messages)):
        for j in range(0, len(messages)):
            msg_sum = add_str(messages[i], messages[j])
            zeros_for_couple[i, j] = calc_zeros_perc(msg_sum)

    plt.imshow(zeros_for_couple, norm=LogNorm())
    plt.show()
