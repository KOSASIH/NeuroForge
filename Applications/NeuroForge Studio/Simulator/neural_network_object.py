data_set = DataSet("data.data", 4, 1)

neural_network = NeuralNetwork(4, [3, 2], 1)

simulator = Simulator(neural_network, data_set)

simulator.simulate(0.01, 1000, 10, print_cost=True)
