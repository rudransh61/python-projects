import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Parameters
POPULATION_SIZE = 100  # Reduce population size for faster computation
NUM_POLYGONS = 10  # Increase number of polygons for more complex images
MAX_VERTICES = 20  # Reduce maximum vertices for simpler polygons
IMAGE_WIDTH = 150  # Decrease image size for faster processing
IMAGE_HEIGHT = 150
NUM_GENERATIONS = 50  # Decrease the number of generations
MUTATION_RATE = 0.2  # Increase mutation rate for more exploration
ELITISM_RATIO = 0.1


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

def fitness(target_image, generated_image):
    diff = np.array(target_image) - np.array(generated_image)
    return np.sum(np.abs(diff))

def draw_individual(individual):
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    for vertices, color in individual:
        draw_polygon(draw, vertices, color)
    return image

def mutate_individual(individual):
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

def evolve(population, target_image):
    graded = [(fitness(target_image, draw_individual(ind)), ind) for ind in population]
    graded = [x[1] for x in sorted(graded)]
    fittest_parents = graded[:int(ELITISM_RATIO * POPULATION_SIZE)]

    offspring = []

    for _ in range(POPULATION_SIZE - len(fittest_parents)):
        parent1 = random.choice(fittest_parents)
        parent2 = random.choice(fittest_parents)
        child = crossover(parent1, parent2)
        if random.random() < MUTATION_RATE:
            child = mutate_individual(child)
        offspring.append(child)

    next_generation = fittest_parents + offspring

    return next_generation

def main(target_image_path):
    target_image = Image.open(target_image_path).resize((IMAGE_WIDTH, IMAGE_HEIGHT))

    population = [generate_individual() for _ in range(POPULATION_SIZE)]

    for i in range(NUM_GENERATIONS):
        population = evolve(population, target_image)
        print(f"Generation {i + 1} completed")

    last_generation = population[-1]
    result_image = draw_individual(last_generation)
    img_num = np.random.randint(1,1000)
    result_image.save(f"result_image{img_num}.png")
    print(f"Result image saved as 'result_image{img_num}.png'")

if __name__ == "__main__":
    main("circle.jpg")
