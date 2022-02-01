import random
from math import sqrt

from Particle import Particle


def normalize_dy(dx, vector_len):
    dy = sqrt(abs(vector_len ** 2 - dx ** 2))
    return dy
    

def explosion(pos, amount=300, explosion_radius=10, gravity=0.2):
    particles = [Particle(random.randint(3, 7), pos, (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))) for _ in range(amount)]

    for i, particle in enumerate(particles):

        vector_len = random.random() * explosion_radius
        dx = random.randint(round(-vector_len * 100), round(vector_len * 100)) / 100
        dy = normalize_dy(dx, vector_len) * random.choice([-1, 1])

        particles[i].direction = dx, dy
        particles[i].shrink_speed = random.random() / 2
        particles[i].gravity = gravity
        particles[i].trace_shrink_speed = random.randint(50, 100) / 100

    return particles
