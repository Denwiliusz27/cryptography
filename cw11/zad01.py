import math
from qiskit import QuantumCircuit, BasicAer, execute
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# zwraca entropie Shanona dla podanej listy
def entropy(probs):
    sum = 0

    for i in range(len(probs)):
        sum += probs[i] * math.log(probs[i], 2)

    return -sum



def create_quantum_circuit(n):
    qc = QuantumCircuit(n, n)

    qc.h(range(n))
    qc.measure(range(n), range(n))

    qc.draw(output='mpl', filename='zad01.png')

    backend = BasicAer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots=1000).result().get_counts()

    list = []
    for key in counts:
        counts[key] = counts[key]/1000
        list.append(counts[key])

    print("entropy (",n , '): ', entropy(list))

    name = 'zad01_' + str(n) + '.png'
    plot_histogram(counts, filename=name)


def create_quantum_circuit_with_R(n, theta):
    qc = QuantumCircuit(n, n)

    qc.ry(theta, range(n))
    qc.measure(range(n), range(n))

    backend = BasicAer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots=1000).result().get_counts()

    list = []
    for key in counts:
        counts[key] = counts[key] / 1000
        list.append(counts[key])

    entr = entropy(list)
    print("entropy (n=", n, ',thata:', theta, '): ', entr)
    return entr


if __name__ == '__main__':
    print(entropy([1]) == 0)
    print(entropy([1 / 2, 1 / 2]) == 1)
    print(entropy([1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8]) == 3)
    print(entropy([1 / 3, 1 / 3, 1 / 8, 1 / 9, 1 / 11, 5 / 792]) == 2.144482095549925)

    create_quantum_circuit(4)
    create_quantum_circuit(7)
    create_quantum_circuit(10)

    theta = 0
    thetas = []
    entropies = []

    while theta <= 360:
        entropies.append(create_quantum_circuit_with_R(4, theta))
        thetas.append(theta)
        theta += 15

    plt.clf()
    plt.bar(thetas, entropies, color='red')
    plt.title('Bar chart')
    plt.xlabel('theta')
    plt.ylabel('entropy')
    plt.show()