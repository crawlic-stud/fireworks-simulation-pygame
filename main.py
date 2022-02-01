import pygame
from effects import explosion, explosion
from Effect import Effect
from config import *


class App:
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Fireworks demonstration')
    
    def __init__(self):
        self.running = True
        self.effect = Effect()
        self.mouse_press = False

    def update(self):
        self.CLOCK.tick(FPS)
        self.SCREEN.fill(BACKGROUND)
        [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]

        mouse_pos = pygame.mouse.get_pos()
        self.effect.draw(self.SCREEN)
        
        if pygame.mouse.get_pressed()[0]:
            if not self.mouse_press:
                self.effect.append(explosion(mouse_pos))
                self.mouse_press = True
        else:
            self.mouse_press = False

        pygame.display.update()

    def run(self):
        while self.running:
            print(f'Particles on screen: {len(self.effect.particles)}')
            self.update()


if __name__ == '__main__':
    App().run()
