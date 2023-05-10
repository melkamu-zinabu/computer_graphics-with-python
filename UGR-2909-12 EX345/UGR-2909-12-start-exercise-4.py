import pygame as pg
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GLU import *


vertices = [
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),  # front top right()
    (-1, 1, 1),  # front top left(3)

    (-1, -1, -1),  # back bottom left(4)
    (1, -1, -1),  # back bottom right(5)
    (1, 1, -1),  # back top right (5)
    (-1, 1, -1),  # backtop left(7)
]

faces = [
    (0, 1, 2, 3),  # front face
    (3, 2, 6, 7),  # top face
    (7, 6, 5, 4),  # back face
    (4, 5, 1, 0),  # bottom face
    (1, 5, 6, 2),  # right face
    (4, 0, 3, 7),  # left face
]

colors = [
    (1, 0, 0, 1),  # RED(front face)
    (0, 1, 0, 1),  # GREEN(top face)
    (0, 0, 1, 1),  # BLUE(back face)
    (1, 1, 0, 1),  # YELLOW(bottom face)
    (1, 0, 1, 1),  # magenta(right face)
    (0, 1, 1, 1),
]


def draw_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor4f(*colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()


def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)
    glTranslatef(0.0, 0.0, -5.0)

    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 1, 1, 1)
        draw_cube()
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
