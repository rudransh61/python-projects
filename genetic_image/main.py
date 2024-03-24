import random
import numpy as np
from PIL import Image, ImageDraw
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Parameters
POPULATION_SIZE = 100
NUM_POLYGONS = 50
MAX_VERTICES = 30
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200
NUM_GENERATIONS = 100
INITIAL_MUTATION_RATE = 0.05
MAX_MUTATION_RATE = 0.5

# Load target image
target_image = Image.open("milees.jpg").convert("RGB")

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
    
    # Convert images to numpy arrays
    target_array = np.array(target_image)
    generated_array = np.array(image)
    
    # Compute Mean Squared Error (MSE)
    mse = mean_squared_error(target_array, generated_array)
    
    # Return the negative of MSE as fitness score (since we want to maximize fitness)
    return -mse


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
        parent1 = graded[0]  # Select the individual with the highest fitness as parent1
        parent2 = random.choice(graded)  # Randomly select parent2 from the graded population

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

    # Lists to store generation number and best fitness score
    generation_numbers = []
    best_fitness_scores = []

    # Evolution loop
    for generation in range(1, NUM_GENERATIONS + 1):
        population = evolve(population, mutation_rate)
        best_fitness = fitness(population[0])
        print(f"Generation {generation}: Best Fitness - {best_fitness}")

        # Append generation number and best fitness score to lists
        generation_numbers.append(generation)
        best_fitness_scores.append(best_fitness)

        # Increase mutation rate gradually
        mutation_rate = min(MAX_MUTATION_RATE, mutation_rate * 1.1)

        # Visualize best solution
        if generation == NUM_GENERATIONS:
            best_individual = population[0]
            best_image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
            draw = ImageDraw.Draw(best_image)
            for vertices, color in best_individual:
                draw_polygon(draw, vertices, color)
            plt.imshow(best_image)
            plt.title(f"Generation {generation}: Best Fitness - {best_fitness}")
            plt.show()

    # Save last image regardless of interrupt
    best_individual = population[0]
    best_image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(best_image)
    for vertices, color in best_individual:
        draw_polygon(draw, vertices, color)
    img = np.random.randint(1000)
    best_image.save(f"result_image_{img}.png")
    print(f"Last generation image saved as result_image_{img}.png.")

    # Plot the evolution of fitness scores
    plt.plot(generation_numbers, best_fitness_scores)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.title('Evolution of Fitness Scores')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
