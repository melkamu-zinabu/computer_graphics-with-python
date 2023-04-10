import pygame as pg
from OpenGL.GL import *
import numpy as np
import ctypes
from OpenGL.GL.shaders import compileProgram, compileShader
import os



class Triangle:
    def init(self):
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.0, 0.5, 0.0, 1.0, 0.0, 0.0,
        )
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,
                              24, ctypes.c_void_p(12))
    # def draw(self):
    #     glBindVertexArray(1, (self.vao))
    #     glDrawArrays(GL_TRIANGLES,0,3)
        
        

    def display(self):
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)


class App:
    def init(self):
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)

        vertex_path = os.path.join(os.path.dirname(__file__),
                                   "/shader/vertex.txt")
        fragment_path = os.path.join(os.path.dirname(__file__),
                                     "/shader/fragment.txt")
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
            glClear(GL_COLOR_BUFFER_BIT)
            glColor3f(1.0, 0.0, 0.0)  # Set the current color to red
            self.triangle.display()
            pg.display.flip()
            self.clock.tick(60)

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