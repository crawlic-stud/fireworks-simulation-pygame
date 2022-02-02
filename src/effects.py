import random
from math import sqrt

from Particle import Particle
from config import HEIGHT


def normalize_dy(dx, vector_len):
    dy = sqrt(abs(vector_len ** 2 - dx ** 2))
    return dy
    

def explosion(pos, amount=100, explosion_radius=7, ball_radius=3, gravity=0.2, ball_lifespan=5, trace_lifespan=1):
    particles = [Particle(ball_radius, pos, (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))) for _ in range(amount)]

    for i, particle in enumerate(particles):

        vector_len = random.random() * explosion_radius
        dx = random.randint(round(-vector_len * 100), round(vector_len * 100)) / 100
        dy = normalize_dy(dx, vector_len) * random.choice([-1, 1])

        particles[i].direction = dx, dy
        particles[i].shrink_speed = random.random() / ball_lifespan
        particles[i].gravity = gravity
        particles[i].trace_shrink_speed = random.randint(30, 50) / 100 / trace_lifespan

    return particles


def launch(x_pos, amount=10, gravity=0.1):
    particles = [Particle(random.randint(2, 3), (x_pos, HEIGHT), (255, 204, 102)) for _ in range(amount)]

    for i, particle in enumerate(particles):

        dy = random.randint(-150, -80) / 10
        dx = random.random() * random.choice([-1, 1])

        particles[i].direction = dx, dy
        particles[i].shrink_speed = random.random() / 100
        particles[i].gravity = gravity
        particles[i].trace_shrink_speed = random.randint(30, 50) / 500

    return particles
