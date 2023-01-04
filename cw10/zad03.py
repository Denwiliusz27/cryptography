from qiskit import QuantumCircuit, BasicAer, execute, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_histogram
import numpy as np


if __name__ == '__main__':
    qc = QuantumCircuit(1, 1)
    qc.u(np.pi / 3, np.pi, np.pi, 0)
    qc.measure([0], [0])

    backend = BasicAer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots=8196).result().get_counts()
    for key in counts:
        counts[key] = counts[key]/8196

    print(counts)
    plot_histogram(counts, filename="zad03_hist.png")

    cr1 = ClassicalRegister(1, name='cr1')
    cr2 = ClassicalRegister(1, name='cr2')
    cr3 = ClassicalRegister(1, name='cr3')

    qr = QuantumRegister(3, name='q')
    qc = QuantumCircuit(qr, cr1, cr2, cr3)

    qc.u(np.pi / 3, np.pi, np.pi, 0)
    qc.barrier()
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()
    qc.measure([0, 1], [0, 1])
    qc.barrier()
    qc.x(2).c_if(cr2, 1)
    qc.z(2).c_if(cr1, 1)
    qc.barrier()
    qc.measure([2], [2])
    qc.draw(output='mpl', filename="zad03.png")

    backend = BasicAer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots=8196).result().get_counts()

    counts_last = {0: 0, 1: 0}

    for key in counts:
        if key[0] == '1':
            counts_last[1] += counts[key]
        else:
            counts_last[0] += counts[key]

    for key in counts_last:
        counts_last[key] = counts_last[key]/8196

    print(counts_last)
    plot_histogram(counts_last, filename="zad03_final_hist.png")