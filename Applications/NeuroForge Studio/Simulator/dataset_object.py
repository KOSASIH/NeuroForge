data_set =
```Here's an example of how you can use the `Simulator` and `DataSet` classes to simulate your neural network:

First, let's create a `NeuralNetwork` class:
```python
import numpy as np

class NeuralNetwork:
    def __init__(self, num_inputs, num_hidden_layers, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_outputs = num_outputs

        self.weights = []
        self.biases = []

        for i in range(num_hidden_layers + 1):
            if i == 0:
                self.weights.append(np.random.randn(num_inputs, num_hidden_layers[0]))
                self.biases.append(np.random.randn(num_hidden_layers[0]))
            elif i == num_hidden_layers:
                self.weights.append(np.random.randn(num_hidden_layers[-1], num_outputs))
                self.biases.append(np.random.randn(num_outputs))
            else:
                self.weights.append(np.random.randn(num_hidden_layers[i - 1], num_hidden_layers[i]))
                self.biases.append(np.random.randn(num_hidden_layers[i]))

    def train(self, inputs, learning_rate):
        self.forward_propagation(inputs)
        self.backward_propagation(inputs, learning_rate)

    def predict(self, inputs):
        outputs = self.forward_propagation(inputs)
        return outputs

    def forward_propagation(self, inputs):
        self.layer_values = [inputs]

        for i in range(self.num_hidden_layers):
            self.layer_values.append(np.maximum(0, np.dot(self.layer_values[-1], self.weights[i]) + self.biases[i]))

        self.layer_values.append(np.dot(self.layer_values[-1], self.weights[-1]) + self.biases[-1])

        return self.layer_values[-1]

    def backward_propagation(self, inputs, learning_rate):
        delta = 2 * (self.predict(inputs) - inputs) * self.sigmoid_derivative(self.layer_values[-1])

        for i in range(self.num_hidden_layers, 0, -1):
            self.weights[i] += learning_rate * np.dot(self.layer_values[i - 1].T, delta)
            self.biases[i] += learning_rate * delta

            delta = np.dot(delta, self.weights[i - 1].T) * self.sigmoid_derivative(self.layer_values[i - 1])

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
