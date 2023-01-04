from qiskit import QuantumCircuit, BasicAer, execute, QuantumRegister, ClassicalRegister, IBMQ, assemble
from qiskit.visualization import plot_histogram

if __name__ == '__main__':
    qc = QuantumCircuit(3,3)

    # 001
    # qc.initialize('1', 2)

    # 010
    # qc.initialize('1', 1)

    qc.h(0)
    qc.cx(0,1)
    qc.x(1)
    qc.cx(1,2)
    qc.cx(0,2)


    qc.measure([0,1,2],[0,1,2])
    qc.draw(output='mpl', filename='zad01.png')

    backend = BasicAer.get_backend('qasm_simulator')
    counts = execute(qc, backend, shots=1000).result().get_counts()

    for key in counts:
        counts[key] = counts[key]/1000

    print(counts)
    plot_histogram(counts, filename='zad01_000.png')