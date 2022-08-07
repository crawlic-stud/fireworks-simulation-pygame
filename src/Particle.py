import pygame

IMAGE = pygame.image.load("images/particle.png")


class Particle:
    def __init__(self, radius, pos, color=(255, 255, 0), trace_delay=0):
        self.radius = radius
        self.x, self.y = pos
        self.color = color
        self.direction = 0, 0
        self.shrink_speed = 0
        self.visibility = 255

        image_size = (round(radius), round(radius))
        image = IMAGE.convert_alpha()
        image.fill(self.color + (0,), None, pygame.BLEND_RGBA_MAX)
        self.image = pygame.transform.scale(image, image_size)

        self.gravity = 0
        self.vertical_speed = self.gravity

        self.trace_shrink_speed = 0
        self.trace_delay = trace_delay
        self.trace_delay_count = 0

    def shrink(self, step=5):
        if not self.shrink_speed:
            return
        self.radius -= self.shrink_speed
        self.visibility -= step
        self.image.fill((0, 0, 0, step), None, pygame.BLEND_RGBA_SUB)

    def move(self):
        if not any(self.direction):
            return
        self.x += self.direction[0]
        self.y += self.direction[1]

    def apply_gravity(self):
        self.y += self.vertical_speed
        self.vertical_speed += self.gravity

    def trace(self):
        self.trace_delay_count += 1
        if self.trace_shrink_speed and self.trace_delay_count >= self.trace_delay:
            trace = Particle(self.radius, (self.x, self.y), self.color)
            trace.shrink_speed = self.trace_shrink_speed
            self.trace_delay_count = 0
            return trace

    def update(self, screen):
        self.move()
        self.apply_gravity()
        self.shrink()
        self.draw(screen)

    def draw(self, screen):
        if self.visibility > 0:
            screen.blit(self.image, (self.x, self.y))
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
