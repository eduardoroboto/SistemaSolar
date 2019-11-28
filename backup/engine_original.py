import pygame
from pygame.locals import *
from OpenGL.GLU import *

from shapes import *


if __name__ == "__main__":
    pygame.init()
    display = (700, 700)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # Pode utilizar o Perspective
    gluPerspective(45, display[0]/display[1], 0.1, 1000000.0 )
    glTranslate(0.0, 0.0, -50)

    #glEnable(GL_BLEND)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    # quad2 = Square(0, 0, 7)
    # quad = Rectangle(0, 0, 5,5)


    linex = Line(-100,0,0,100,0,0,color=(1,0,0))
    liney = Line(0,-100,0,0,100,0,color=(0,1,0))
    linez = Line(0,0,-100,0,0,100,color=(0,0,1))

    triangulo = Triangle((0, 0, 0), (4, 0, 0), (2, 4, 0))
    quadrado = Square(0, 0, 10)
    retangulo = Rectangle(0, 0, 3, 6)
    circulo = Circle(5, 5, 5, 20)
    cubo = Cube(0, 0, 0, 5)
    ponto = Vertex(2, 2)
    esfera = Sphere(5, 5, 0, 5, 20)
    giza = Pyramid(0, 0, 0, 15, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("clicado")
                    #quad2.draw()

        #
        # mouseMove = pygame.mouse.get_rel()
        #
        # glRotate(mouseMove[0] * 0.2, 0.0, 1.0, 0.0)
        # glRotate(mouseMove[1] * 0.2, 1.0, 0.0, 0.0)

        # glRotate(1,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)




        linex.draw()
        liney.draw()
        linez.draw()

        triangulo.draw() #Ok
        # triangulo.reflection() #OK
        # triangulo.translation(1,0,0) #OK
        # triangulo.rotation(1,'y') #OK
        # triangulo.scale(1.1,1.1,1.1) #OK
        # quadrado.draw() # OK
        # quadrado.reflection(1) #OK
        # quadrado.rotation(1,'y') #Ok
        # quadrado.translation(1,0) #OK
        # retangulo.draw() #OK
        # retangulo.rotation(1,'z') #Ok
        # retangulo.reflection(2) #OK
        # circulo.draw() #OK
        # circulo.reflection() #OK
        # circulo.rotation(1,'z') #OK
        # circulo.translation(1,0) #OK
        # cubo.draw() #OK
        # cubo.reflection(1) #NOT OK
        # cubo.translation(1,0,0) #OK
        # cubo.rotation(1,'z') #OK
        # esfera.draw() #OK
        # esfera.reflection(2)   #OK
        # esfera.rotation(1,'y')  #OK
        # esfera.translation(0,0,0) #OK

        # giza.draw() #OK
        # giza.reflection() #NOT OK
        # giza.rotation(1,'y') #NOT OK
        # giza.translation(1,0,0) #NOT OK

        linex.draw()
        liney.draw()
        linez.draw()

        pygame.display.flip()
        pygame.time.wait(100)
