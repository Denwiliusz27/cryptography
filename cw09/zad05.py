import hashlib
import sys
import matplotlib.pyplot as plt
import random


def mine(diff):
    m = hashlib.sha256()
    zeros = '0' * int(diff)

    for i in range(100000):
        m.update(bytes(i))
        value = m.hexdigest()

        if value[0:int(diff)] == zeros:
            return i
        i += 1

    return -1000


def mine_random(diff):
    m = hashlib.sha256()
    zeros = '0' * int(diff)
    # print("zeros: ", zeros, ", diff: ", diff)

    for i in range(100000):
        v = random.randint(0, 100000)
        m.update(bytes(v))
        value = m.hexdigest()

        if value[0:int(diff)] == zeros:
            return i

    return -1000



if __name__ == '__main__':
    d_values = []
    id_values = []

    for d in range(6):
        id = mine(str(d))
        d_values.append(d)
        id_values.append(id)

    plt.scatter(d_values, id_values)
    plt.xlabel("d")
    plt.yscale('symlog')
    plt.ylabel("i(d)")
    # plt.show()

    d_values = []
    id_values = []

    for d in range(6):
        id = mine_random(str(d))
        d_values.append(d)
        id_values.append(id)

    plt.scatter(d_values, id_values, color = "red")
    plt.xlabel("d")
    plt.yscale('symlog')
    plt.ylabel("i(d)")
    plt.show()
