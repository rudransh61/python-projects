import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Organic Particle Life Simulation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
        self.speed = 0
        self.direction = 0

    def apply_force(self, force):
        self.speed += force

    def move(self):
        noise = random.uniform(-0.1, 0.1)  # Random noise added to direction
        self.direction += noise
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Function to calculate distance between two particles
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Function to apply forces between particles
def apply_forces(particles):
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1, p2 = particles[i], particles[j]
            dist = distance(p1, p2)
            if dist != 0:
                force = 10 / dist  # Weak force
                if dist < 100:  # Attraction
                    force *= -1
                if dist > 200:  # Repulsion
                    force *= 2  # Increase repulsion force
                angle = math.atan2(p2.y - p1.y, p2.x - p1.x)
                p1.apply_force(force)
                p1.direction = angle
                p2.apply_force(force)
                p2.direction = angle + math.pi

# Create particles
num_particles = 100
particles = []
for _ in range(num_particles):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particle = Particle(random.randint(0, width), random.randint(0, height), color)
    particle.speed = random.uniform(0.1, 1)  # Random initial speed
    particle.direction = random.uniform(0, 2 * math.pi)  # Random initial direction
    particles.append(particle)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply forces between particles
    apply_forces(particles)
    
    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw()

    pygame.display.flip()
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
