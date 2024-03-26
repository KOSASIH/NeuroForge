import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

def create_population(population_size, input_size, output_size):
    population = []
    for _ in range(population_size):
        network = MLPClassifier(hidden_layer_sizes=(input_size,), max_iter=100)
        mutation_rate = random.uniform(0.01, 0.5)
        population.append((network, mutation_rate))
    return population

def mutate(network, mutation_rate):
    new_network = MLPClassifier(hidden_layer_sizes=network.hidden_layer_sizes, max_iter=100)
    for i in range(len(network.coefs_[0])):
        for j in range(len(network.coefs_[0][0])):
            if random.random() < mutation_rate:
                new_network.coefs_[0][i][j] = random.gauss(0, 1)
                new_network.intercepts_[0][i] = random.gauss(0, 1)
    return new_network

def crossover(parent1, parent2):
    child = MLPClassifier(hidden_layer_sizes=parent1.hidden_layer_sizes, max_iter=100)
    crossover_point = random.randint(0, len(parent1.coefs_[0]))
    child.coefs_[0] = parent1.coefs_[0][:crossover_point] + parent2.coefs_[0][crossover_point:]
    child.intercepts_[0] = parent1.intercepts_[0][:crossover_point] + parent2.intercepts_[0][crossover_point:]
    return child

def evolve_population(population, input_data, output_data, generations):
    for generation in range(generations):
        new_population = []
        for i in range(0, len(population), 2):
            parent1, mutation_rate1 = population[i]
            parent2, mutation_rate2 = population[i + 1]
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate1)
            new_population.append((child, mutation_rate1))
            child = mutate(parent2, mutation_rate2)
            new_population.append((child, mutation_rate2))
        population = new_population
        best_network = max(population, key=lambda x: accuracy_score(output_data, x[0].predict(input_data)))[0]
        print(f"Generation {generation + 1}: Best accuracy = {accuracy_score(output_data, best_network.predict(input_data))}")
    return best_network

input_data, output_data = load_data()
input_size = len(input_data[0])
output_size = len(set(output_data))
population_size = 10
generations = 10

best_network = evolve_population(create_population(population_size, input_size, output_size), input_data, output_data, generations)
