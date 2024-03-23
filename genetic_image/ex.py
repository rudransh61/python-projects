import numpy as np
import cv2
from skimage.color import deltaE_cie76
from skimage import io

class GeneticAlgorithmImageRecreation:
    def __init__(self, target_image_path, initial_population_size=50, mutation_probability=0.05):
        self.target_image = io.imread(target_image_path)
        self.initial_population_size = initial_population_size
        self.mutation_probability = mutation_probability

    def generate_initial_population(self):
        initial_population = []
        for _ in range(self.initial_population_size):
            individual = np.random.randint(0, 256, size=self.target_image.shape, dtype=np.uint8)
            initial_population.append(individual)
        return initial_population

    def calculate_fitness(self, individual):
        return deltaE_cie76(self.target_image, individual)

    def tournament_selection(self, population, k=8):
        selected_parents = []
        for _ in range(len(population)):
            tournament = np.random.choice(population, k, replace=False)
            winner = min(tournament, key=self.calculate_fitness)
            selected_parents.append(winner)
        return selected_parents

    def blend_crossover(self, parent1, parent2):
        alpha = np.random.uniform(0, 1, size=parent1.shape)
        child = (alpha * parent1) + ((1 - alpha) * parent2)
        return child.astype(np.uint8)

    def mutation_random_shape(self, individual):
        shape = np.random.randint(0, 256, size=self.target_image.shape, dtype=np.uint8)
        return individual + shape

    def mutation_add_constant(self, individual):
        constant = np.random.randint(-50, 50)
        mask = np.random.choice([True, False], size=self.target_image.shape)
        individual[mask] += constant
        return individual

    def apply_mutation(self, individual):
        mutation_functions = [self.mutation_random_shape, self.mutation_add_constant]
        mutation_probabilities = [0.5, 0.5]
        for func, prob in zip(mutation_functions, mutation_probabilities):
            if np.random.rand() < prob:
                individual = func(individual)
        return individual

    def evolve(self, num_generations):
        population = self.generate_initial_population()
        for generation in range(num_generations):
            parents = self.tournament_selection(population)
            offspring = []
            while len(offspring) < len(population):
                parent1, parent2 = np.random.choice(parents, 2, replace=False)
                child = self.blend_crossover(parent1, parent2)
                if np.random.rand() < self.mutation_probability:
                    child = self.apply_mutation(child)
                offspring.append(child)
            population = offspring
        best_individual = min(population, key=self.calculate_fitness)
        return best_individual

# Example usage:
target_image_path = "spider.jpg"
genetic_algorithm = GeneticAlgorithmImageRecreation(target_image_path)
best_image = genetic_algorithm.evolve(num_generations=100)
cv2.imwrite("recreated_image.jpg", best_image)
