import algorithms

class CognitiveComputing:
    def __init__(self, name):
        self.name = name
        self.algorithm = None

    def set_algorithm(self, algorithm_name):
        if algorithm_name == "algorithm1":
            self.algorithm = algorithms.algorithm1.Algorithm1()
        elif algorithm_name == "algorithm2":
            self.algorithm = algorithms.algorithm2.Algorithm2()
        else:
            raise ValueError("Invalid algorithm name")

    def run(self, input_data):
        return self.algorithm.run(input_data)

if __name__ == "__main__":
    cognitive_computing = CognitiveComputing("My Cognitive Computing")
    cognitive_computing.set_algorithm("algorithm1")
    input_data = ...
    output_data = cognitive_computing.run(input_data)
