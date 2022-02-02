import numpy as np
import pygame
from effects import explosion
from Effect import Effect
from config import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
pygame.init()


with open("vertex.glsl", 'r') as f:
    vertex_src = f.read()

with open("fragment.glsl", 'r') as f:
    fragment_src = f.read()


class App:
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption('Fireworks simulation')

    def __init__(self):
        self.running = True

        self.refactor = None
        self.triangle_buffer = None
        self.buffer_data = None

    def update(self):
        self.CLOCK.tick(FPS)

        # cleaning buffer
        glClear(GL_COLOR_BUFFER_BIT)

        # draw triangle
        glDrawArrays(GL_POLYGON, 0, 3)

        [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]

        pygame.display.flip()

    def setup(self):
        # setting background color
        glClearColor(*[color / 255 for color in BACKGROUND], 1)

        # create array
        self.refactor = np.array([
            # x   y    z       r         g          b
            1.0, 1.0, 0.0, 52 / 255, 178 / 255, 152 / 255,
            -0.5, -0.5, 0.0, 57 / 255, 151 / 255, 211 / 255,
            0.5, -0.5, 0.0, 81 / 255, 179 / 255, 15 / 255,
            -0.5, 1.0, 0.0, 23 / 255, 100 / 255, 201 / 255,
        ], dtype=np.float32)

        # create buffer
        self.triangle_buffer = glGenBuffers(1)

        # bind buffer to load data
        glBindBuffer(GL_ARRAY_BUFFER, self.triangle_buffer)

        # load array data to buffer
        glBufferData(GL_ARRAY_BUFFER, self.refactor.nbytes, self.refactor, GL_STATIC_DRAW)

        # read buffer data
        self.buffer_data = glGetBufferSubData(GL_ARRAY_BUFFER, 0, self.refactor.nbytes)

        # compile vertex shader
        vertex_shader = compileShader(vertex_src, GL_VERTEX_SHADER)
        
        # compile fragment shader
        fragment_shader = compileShader(fragment_src, GL_FRAGMENT_SHADER)

        # link shaders to a program
        shader_program = compileProgram(vertex_shader, fragment_shader)

        # make shader program active
        glUseProgram(shader_program)

        # vertex positions -> vertex shader
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.refactor.itemsize * 6, ctypes.c_void_p(0))

        # color -> vertex shader
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, self.refactor.itemsize * 6, ctypes.c_void_p(self.refactor.itemsize * 3))

    def run(self):
        self.setup()
        while self.running:
            self.update()


if __name__ == '__main__':
    App().run()
