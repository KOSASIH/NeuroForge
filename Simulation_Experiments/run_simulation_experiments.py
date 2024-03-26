# Import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt

# Define paths and network parameters
path_data = "~/Documents/neuroforge_data"
num_experiments = 100
num_neurons = 1000
input_size = 10
output_size = 10
learning_rate = 0.01

# Define function for creating synthetic data
def generate_synthetic_data(input_size, num_samples):
    """
    Generate synthetic data for simulation experiments
    """
    X = np.random.rand(num_samples, input_size)
    Y = np.random.rand(num_samples, output_size)

    return X, Y

# Define function for running simulation experiments
def run_simulation_experiments(num_experiments, num_neurons, input_size, output_size, learning_rate, path_data):
    """
    Run simulation experiments using the synthetic data
    """
    X, Y = generate_synthetic_data(input_size, num_samples=100)

    for i in range(num_experiments):
        # Create a random network with the specified number of neurons
        network = np.random.rand(input_size, num_neurons, output_size)

        # Run the simulation for a specified number of iterations
        for iteration in range(500):
            # Forward pass
            output = network.dot(X)

            # Backpropagation
            error = output - Y
            delta = error.dot(network.T)
            network -= learning_rate * delta

        # Save the results
        np.save(os.path.join(path_data, f"experiment_{i}.npy"), network)

        # Plot the results
        if i % 10 == 0:
            plt.plot(np.absolute(network))
            plt.title(f"Experiment {i}")
            plt.show()

# Run simulation experiments
run_simulation_experiments(num_experiments, num_neurons, input_size, output_size, learning_rate, path_data)
