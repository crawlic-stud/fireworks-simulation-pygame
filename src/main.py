import random

import pygame

from effects import explosion, launch
from Effect import Effect
from config import *

pygame.init()
pygame.mixer.init()


explosion_sounds = [pygame.mixer.Sound('sounds/explosion_long.wav'), pygame.mixer.Sound('sounds/explosion_short.wav')]


class App:
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Fireworks simulation')
    
    def __init__(self):
        self.running = True
        self.firework_effect = Effect()
        self.launch_effect = Effect()
        self.mouse_press = False

    def update(self):
        self.CLOCK.tick(FPS)
        self.SCREEN.fill(BACKGROUND)
        [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]

        mouse_pos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            if not self.mouse_press:
                self.launch_effect.append(launch(x_pos=mouse_pos[0],
                                                 amount=3,
                                                 gravity=0.15,
                                                 trace_delay=0))
                self.mouse_press = True
        else:
            self.mouse_press = False

        for particle in self.launch_effect.particles:
            if particle.vertical_speed > abs(particle.direction[1]):
                self.launch_effect.particles.remove(particle)

                trace_lifespan = random.randint(1, 1)
                ball_radius = random.randint(5, 8)
                ball_lifespan = 3
                explosion_radius = random.randint(4, 6)
                amount = random.randint(150, 200)
                self.firework_effect.append(explosion(pos=(particle.x, particle.y),
                                                      amount=amount,
                                                      explosion_radius=explosion_radius,
                                                      ball_radius=ball_radius,
                                                      ball_lifespan=ball_lifespan,
                                                      trace_lifespan=trace_lifespan,
                                                      gravity=0.05,
                                                      trace_delay=999))
                random.choice(explosion_sounds).play()

        self.firework_effect.draw(self.SCREEN)
        self.launch_effect.draw(self.SCREEN)

        pygame.display.update()

    def run(self):
        while self.running:
            print(f'Particles on screen: {len(self.firework_effect.particles) + len(self.launch_effect.particles)}')
            self.update()


if __name__ == '__main__':
    App().run()
