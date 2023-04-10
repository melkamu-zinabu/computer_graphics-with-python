import pygame as pg
from OpenGL.GL import *
#COMMENT
import numpy as np

# it is for enmpty screen

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
# it for drawing triangle
   
# class triangle:
#     def __init__(self):
#         self.vertices={


#         }
#         self.vertices=np.array(self.vertices,dtype=np.float32)
#         self.vao=glGenVertexArrays(1)
#         glBindVertexBuffer(self.vao)
#         self.vao=glBindBuffer(GL_ARRAY_BUFFER,self.vao)
#         glBufferData(
#             GL_ARRAY_BUFFER,
#             self.vertices.nbytes,
#             self.vertices,
#             GL_STATIC_DRAW)
#         glEnableVertexArrayAttrib(0)
#         glVertexAttribPointer(
#             0,3,
#             GL_FLOAT,GL_FALSE,24,
#             ctypes.c_void_p(0)
#         )

#         glEnableVertexArrayAttrib(1)
#         glVertexAttribPointer(
#             1,3,
#             GL_FLOAT,GL_FALSE,24,
#             ctypes.c_void_p(12)
#         )
#     def destroy(self):
#         glDeleteVertexArrays(1,(self.vao))
#         glDeleteBuffers

if __name__=="__main__":
    #intialize window
    app=App()

# import pygame
# import math

# # Initialize Pygame
# pygame.init()

# # Set the window size
# screen_width = 500
# screen_height = 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# # Set the title of the window
# pygame.display.set_caption("My Game")

# # Set the color of the triangle
# triangle_color = (255, 0, 0)

# # Set the position and size of the triangle
# triangle_side = 100
# triangle_height = math.sqrt(3) / 2 * triangle_side
# triangle_x = (screen_width - triangle_side) / 2
# triangle_y = (screen_height - triangle_height) / 2
# triangle_points = [(triangle_x, triangle_y + triangle_height),
#                    (triangle_x + triangle_side / 2, triangle_y),
#                    (triangle_x + triangle_side, triangle_y + triangle_height)]

# # Game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen
#     screen.fill((255, 0, 255))

#     # Draw the triangle
#     pygame.draw.polygon(screen, triangle_color, triangle_points)

#     # Update the display
#     pygame.display.update()

# # Quit Pygame
# pygame.quit()
