import pygame as pg
from OpenGL.GL import *
#COMMENT
class App:
    #constructor
    def __init__(self) -> None:
        pg.init()
        pg.display.set_mode((640,400),pg.OPENGL|pg.DOUBLEBUF)
        self.clock=pg.time.Clock()
        #creating variable
        glClearColor(0.1,0.2,0.2,1)
        self.mainLoop()
        # the below function
    

    def mainLoop(self):
        running =True
        while running:
            for event in pg.event.get():
                if(event.type==pg.quit):
                    running=False
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()       
            self.clock.tick(60)
   


if __name__=="__main__":
    #intialize window
    app=App()