import random
from config import WIDTH, HEIGHT


class Effect:
    def __init__(self, trace_delay=0):
        self.particles = []

    def append(self, particles_array):
        self.particles += particles_array
        for particle in self.particles:
            self.add_trace(particle)

    def remove_particle(self, particle):
        if any([particle.radius < 0,
                particle.x < -particle.radius, particle.x > WIDTH + particle.radius,
                particle.y < -particle.radius, particle.y > HEIGHT + particle.radius]):
            self.particles.remove(particle)

    def add_trace(self, particle):
        if particle.trace_shrink_speed > 0:
            trace = particle.trace()
            if trace is None:
                return
            self.particles.append(trace)

    def draw(self, screen):
        for particle in self.particles:
            self.add_trace(particle)
            self.remove_particle(particle)
            particle.update(screen)
