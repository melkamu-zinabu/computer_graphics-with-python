import pygame as pg
from OpenGL.GL import *
from pygame.locals import *
import random
from OpenGL.GLU import *
from OpenGL.GLUT import *

MAX_PARTICLES = 1000
PARTICLE_SIZE = 0.2
WIND_FORCE = (-0.05, 0, 0)


class Particle:
    def __init__(self, pos, vel, color):
        self.pos = pos
        self.vel = vel
        self.color = color

    def draw(self):
        glPushMatrix()
        glColor3f(*self.color)
        glTranslate(*self.pos)
        quad = gluNewQuadric()
        gluSphere(quad, PARTICLE_SIZE, 10, 10)
        gluDeleteQuadric(quad)
        glPopMatrix()

    def update(self):
        self.vel = tuple(sum(x) for x in zip(self.vel, WIND_FORCE))
        self.pos = tuple(sum(x) for x in zip(self.pos, self.vel))


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        if len(self.particles) < MAX_PARTICLES:
            self.particles.append(particle)


def main():
    pg.init()
    display = (600, 800)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10.0)

    clock = pg.time.Clock()
    particle_system = ParticleSystem()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        pos = (0, 0, 0)
        vel = (random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), 0)
        color = (random.uniform(0.5, 1.0), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))

        particle_system.add_particle(Particle(pos, vel, color))

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for particle in particle_system.particles:
            particle.draw()
            particle.update()

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
