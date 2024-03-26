import numpy as np
import matplotlib.pyplot as plt
import time

class Simulator:
    def __init__(self, neural_network, data_set, visualization=True):
        self.neural_network = neural_network
        self.data_set = data_set
        self.visualization = visualization

    def simulate(self, learning_rate, num_iterations, batch_size=1, print_cost=True):
        costs = []
        start_time = time.time()

        for i in range(num_iterations):
            mini_batch = self.data_set.get_mini_batch(batch_size)
            self.neural_network.train(mini_batch, learning_rate)

            if i % 100 == 0 and print_cost:
                cost = self.neural_network.calculate_cost(self.data_set.get_training_inputs(), self.data_set.get_training_outputs())
                costs.append(cost)
                print(f"Cost at iteration {i}: {cost}")

        if self.visualization:
            self.visualize_cost(costs, start_time)

    def visualize_cost(self, costs, start_time):
        plt.figure()
        plt.plot(costs)
        plt.xlabel("Iteration")
        plt.ylabel("Cost")
        plt.title(f"Cost vs Iteration (Total time: {round(time.time() - start_time, 2)} seconds)")
        plt.show()
