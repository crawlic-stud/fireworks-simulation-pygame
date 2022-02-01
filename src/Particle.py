import random
import pygame


class Particle:
    def __init__(self, radius, pos, color):
        self.radius = radius
        self.x, self.y = pos
        self.color = color
        self.direction = None
        self.shrink_speed = None

        self.gravity = 0
        self.vertical_speed = self.gravity

        self.trace_shrink_speed = 0

    def shrink(self):
        if self.shrink_speed is None:
            return
        self.radius -= self.shrink_speed

    def move(self):
        if self.direction is None:
            return
        self.x += self.direction[0]
        self.y += self.direction[1]

    def apply_gravity(self):
        self.y += self.vertical_speed
        self.vertical_speed += self.gravity

    def trace(self):
        if self.trace_shrink_speed:
            trace = Particle(self.radius, (self.x, self.y), self.color)
            trace.shrink_speed = self.trace_shrink_speed
            return trace

    def draw(self, screen):
        self.move()
        self.apply_gravity()
        self.shrink()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
