import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *


class Engine():

    def start_pygame(self):
        pygame.init()
        display = (700, 700)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # Pode utilizar o Perspective
        gluPerspective(45, display[0] / display[1], 0.1, 500.0)
        glTranslate(0.0, 0.0, -50)

    def exit_pygame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def mouse_moviment(self):
        mouseMove = pygame.mouse.get_rel()
        glRotate(mouseMove[0] * 0.2, 0.0, 1.0, 0.0)
        glRotate(mouseMove[1] * 0.2, 1.0, 0.0, 0.0)

    def clear_buffer(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def flip_and_clock(self,time):
        pygame.display.flip()
        pygame.time.wait(time)

class Three_Axys_Arrows():
    def __init__(self,size=100):
        self.linex = Line(-size,0,0,size,0,0,color=(1,0,0))
        self.liney = Line(0,-size,0,0,size,0,color=(0,1,0))
        self.linez = Line(0,0,-size,0,0,size,color=(0,0,1))

    def draw(self):
        self.linex.draw()
        self.liney.draw()
        self.linez.draw()

esfera = Sphere(5,5,0,5,10)
triangulo = Triangle((0, 0, 0), (4, 0, 0), (2, 4, 0))

ENGINE = Engine()
ENGINE.start_pygame()
arrows = Three_Axys_Arrows()

if __name__ == "__main__":

    while True:
        ENGINE.exit_pygame()
        ENGINE.clear_buffer()
        arrows.draw()

        ENGINE.mouse_moviment()

        esfera.draw() #OK
        esfera.rotation(5,'y')  #OK

        # triangulo.draw() #Ok
        # triangulo.reflection() #OK
        # triangulo.translation(1,0,0) #OK
        # triangulo.rotation(1,'y') #OK


        ENGINE.flip_and_clock(100)

