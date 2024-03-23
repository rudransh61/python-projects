import random
import numpy as np
from PIL import Image, ImageDraw

# Parameters
POPULATION_SIZE = 100
NUM_POLYGONS = 50
MAX_VERTICES = 30
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
NUM_GENERATIONS = 500
INITIAL_MUTATION_RATE = 0.05
MAX_MUTATION_RATE = 0.1

# Load target image
target_image = Image.open("landscape.jpg").convert("RGB")

def random_color():
    return tuple(np.random.randint(0, 256, size=3))

def random_polygon():
    num_vertices = random.randint(3, MAX_VERTICES)
    vertices = [(random.randint(0, IMAGE_WIDTH), random.randint(0, IMAGE_HEIGHT)) for _ in range(num_vertices)]
    color = random_color()
    return vertices, color

def draw_polygon(draw, vertices, color):
    draw.polygon(vertices, fill=color)

def generate_individual():
    return [random_polygon() for _ in range(NUM_POLYGONS)]

def fitness(individual):
    # Create image based on individual
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    for vertices, color in individual:
        draw_polygon(draw, vertices, color)
    # Resize the image to match the target image dimensions
    image = image.resize((target_image.width, target_image.height))
    
    # Calculate fitness based on pixel-wise difference
    diff = np.array(target_image) - np.array(image)
    return -np.sum(np.abs(diff))  # Negative because we want to maximize fitness

def mutate_individual(individual, mutation_rate):
    mutated_individual = []
    for vertices, color in individual:
        mutated_vertices = [(x + random.randint(-10, 10), y + random.randint(-10, 10)) for x, y in vertices]
        mutated_color = tuple(min(max(c + random.randint(-30, 30), 0), 255) for c in color)
        mutated_individual.append((mutated_vertices, mutated_color))
    return mutated_individual

def crossover(parent1, parent2):
    child = []
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < 0.5:
            child.append(gene1)
        else:
            child.append(gene2)
    return child

def evolve(population, mutation_rate):
    graded = [(fitness(ind), ind) for ind in population]
    graded = [x[1] for x in sorted(graded, key=lambda x: x[0], reverse=True)]  # Sort by fitness

    elites_count = 1  # Number of elites to preserve
    elites = graded[:elites_count]

    offspring = []

    for _ in range(len(population) - elites_count):
        parent1 = random.choice(graded)
        parent2 = random.choice(graded)

        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child = mutate_individual(child, mutation_rate)

        offspring.append(child)

    next_generation = elites + offspring

    return next_generation

def main():
    # Initialize population
    population = [generate_individual() for _ in range(POPULATION_SIZE)]

    mutation_rate = INITIAL_MUTATION_RATE

    # Evolution loop
    for generation in range(1, NUM_GENERATIONS + 1):
        population = evolve(population, mutation_rate)
        best_fitness = fitness(population[0])
        print(f"Generation {generation}: Best Fitness - {best_fitness}")

        # Increase mutation rate gradually
        mutation_rate = min(MAX_MUTATION_RATE, mutation_rate * 1.1)

    # Save best individual from the last generation
    best_individual = population[0]
    best_image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(best_image)
    img = np.random.randint(0,1000)
    for vertices, color in best_individual:
        draw_polygon(draw, vertices, color)
    best_image.save(f"img/result_image{img}.png")
    print(f"Result image saved as 'result_image{img}.png'")

if __name__ == "__main__":
    main()
