class NeuromorphicHardware:
    def __init__(self, name):
        self.name = name
        self.circuits = []

    def add_circuit(self, circuit):
        self.circuits.append(circuit)

    def remove_circuit(self, circuit):
        self.circuits.remove(circuit)

    def simulate(self):
        for circuit in self.circuits:
            circuit.simulate()

if __name__ == "__main__":
    nh = NeuromorphicHardware("My Neuromorphic Hardware")
    c1 = CircuitDesign("Circuit 1")
    c2 = CircuitDesign("Circuit 2")
    nh.add_circuit(c1)
    nh.add_circuit(c2)
    nh.simulate()
