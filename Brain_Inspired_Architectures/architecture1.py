import numpy as np

class Architecture1:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.weights_ih = np.random.randn(hidden_size, input_size)
        self.weights_ho = np.random.randn(output_size, hidden_size)

        self.biases_h = np.zeros(hidden_size)
        self.biases_o = np.zeros(output_size)

    def forward_pass(self, inputs):
        hidden_inputs = np.dot(self.weights_ih, inputs) + self.biases_h
        hidden_outputs = self.sigmoid(hidden_inputs)

        output_inputs = np.dot(self.weights_ho, hidden_outputs) + self.biases_o
        output_outputs = self.sigmoid(output_inputs)

        return output_outputs, hidden_outputs

    def sigmoid(self, x):
        return 1.0/(1 + np.exp(-x))

if __name__ == "__main__":
    architecture1 = Architecture1(input_size=10, hidden_size=5, output_size=2)
    inputs = np.random.randn(1, 10)
    outputs, hidden_states = architecture1.forward_pass(inputs)
