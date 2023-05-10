import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram, compileShader
import os
import math


class Triangle:
    def __init__(self):
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0,
        )
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        vao = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vao)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,
                              24, ctypes.c_void_p(12))
        self.offset_x = 0.0
        self.offset_y = 0.0

    def update(self, dt):
        self.offset_x = math.sin(pg.time.get_ticks() / 1000.0) * 0.2
        self.offset_y = math.cos(pg.time.get_ticks() / 1000.0) * 0.2
        new_vertices = self.vertices.copy()
        new_vertices[0::6] += self.offset_x # Move x of first vertex
        new_vertices[6::6] -= self.offset_x # Move x of second vertex
        new_vertices[12::6] += self.offset_x # Move x of third vertex
        new_vertices[1::6] += self.offset_y # Move y of first vertex
        new_vertices[7::6] += self.offset_y # Move y of second vertex
        new_vertices[13::6] -= self.offset_y # Move y of third vertex
        glBindBuffer(GL_ARRAY_BUFFER, self.vao)
        glBufferSubData(GL_ARRAY_BUFFER, 0, new_vertices.nbytes, new_vertices)

    def display(self):
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)

        vertex_path = os.path.join(os.path.dirname(__file__),
                                   "shader/vertex.txt")
        fragment_path = os.path.join(os.path.dirname(__file__),
                                     "shader/fragment.txt")
        self.shader = self.createShader(vertex_path, fragment_path)
        glUseProgram(self.shader)
        self.triangle = Triangle()
        self.mainloop()

    def mainloop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            dt = self.clock.tick(60) / 1000.0
            glClear(GL_COLOR_BUFFER_BIT)
            self.triangle.update(dt)
            self.triangle.display()
            pg.display.flip()

    def createShader(self, vertexFilePath, fragmentFilePath):
        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()
        with open(fragmentFilePath, 'r') as f:
            fragment_src = f.readlines()
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )
        return shader


if __name__ == "__main__":
    app = App()
