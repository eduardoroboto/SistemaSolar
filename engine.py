import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from shapes import *
# from celestial_object import *
# from global_variables import *
# from planet import *

class Engine():
    def __init__(self,zoom,display):
        self.zoom_factor = -200
        self.display = (700, 700)


    def start_pygame(self,mode="normal"):
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        if mode == "lines":
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # Pode utilizar o Perspective
        gluPerspective(45, self.display[0] / self.display[1], 0.1, 10000000.0)
        glTranslate(0.0, 0.0, self.zoom_factor)

    def user_input(self,mode="ALL"):
        if mode == "ALL" or mode == "mouse":
            mouseMove = pygame.mouse.get_rel()
            glRotate(mouseMove[0] * 0.2, 0.0, 1.0, 0.0)
            glRotate(mouseMove[1] * 0.2, 1.0, 0.0, 0.0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if mode == "ALL" or mode == "zoom":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.zoom_factor=+5
                        glTranslate(0.0, 0.0,  self.zoom_factor)
                    if event.key == pygame.K_DOWN:
                        self.zoom_factor=-5
                        glTranslate(0.0, 0.0, self.zoom_factor)


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

# esfera = Sphere(5,5,0,5,10)
# triangulo = Triangle((0, 0, 0), (4, 0, 0), (2, 4, 0))
#
# ENGINE = Engine()
# ENGINE.start_pygame("lines")
# arrows = Three_Axys_Arrows()
# esfera.revolution_generate(0,0,10,200)


# sun     = Star(0,0,0,RADIUS_MAP(SUN_RADIUS))
# mercury = Planet(0,0,0,RADIUS_MAP(MERCURY_RADIUS))
# venus   = Planet(0,0,0,RADIUS_MAP(VENUS_RADIUS))
# earth   = CelestialObject(0,0,0,RADIUS_MAP(EARTH_RADIUS))
# moon = CelestialObject(0,0,0, RADIUS_MAP(MOON_RADIUS))
# mars    = Planet(0,0,0,RADIUS_MAP(MARS_RADIUS))
# jupiter = Planet(0,0,0,RADIUS_MAP(JUPITER_RADIUS))
# saturn  = Planet(0,0,0,RADIUS_MAP(SATURN_RADIUS ))
# uranus  = Planet(0,0,0,RADIUS_MAP(URANUS_RADIUS ))
# neptune = Planet(0,0,0,RADIUS_MAP(NEPTUNE_RADIUS))
# mercury.revolution_generate(sun.x,sun.y,DISTANCE_MAP(MERCURY_DISTANCE)+sun.radius+mercury.radius,VELOCITY_MAP(MERCURY_VELOCITY))
# venus.revolution_generate(sun.x,sun.y,DISTANCE_MAP(VENUS_DISTANCE)+sun.radius+venus.radius,VELOCITY_MAP(VENUS_VELOCITY))
# earth.revolution_generate(sun.x,sun.y,DISTANCE_MAP(EARTH_DISTANCE)+sun.radius+earth.radius,VELOCITY_MAP(EARTH_VELOCITY))
# mars.revolution_generate(sun.x,sun.y,DISTANCE_MAP(MARS_DISTANCE)+sun.radius+mars.radius,VELOCITY_MAP(MARS_VELOCITY))
# jupiter.revolution_generate(sun.x,sun.y,DISTANCE_MAP(JUPITER_DISTANCE)+sun.radius+jupiter.radius,VELOCITY_MAP(JUPITER_VELOCITY))
# saturn.revolution_generate(sun.x,sun.y,DISTANCE_MAP(SATURN_DISTANCE)+sun.radius+saturn.radius,VELOCITY_MAP(SATURN_VELOCITY))
# uranus.revolution_generate(sun.x,sun.y,DISTANCE_MAP(URANUS_DISTANCE)+sun.radius+uranus.radius,VELOCITY_MAP(URANUS_VELOCITY))
# neptune.revolution_generate(sun.x,sun.y,DISTANCE_MAP(NEPTUNE_DISTANCE)+sun.radius+neptune.radius,VELOCITY_MAP(NEPTUNE_VELOCITY))


#sun = CelestialObject(50, 0)
# sun.spawnMoons(5)


#
# if __name__ == "__main__":
#
#     while True:
#         ENGINE.user_input('zoom')
#         ENGINE.clear_buffer()
#         arrows.draw()
#
#         # arrows.draw()
#         sun.show()
#         # mercury.revolution_animate()
#         # venus.revolution_animate()
#         # earth.revolution_animate()
#         # mars.revolution_animate()
#         # jupiter.revolution_animate()
#         # saturn.revolution_animate()
#         # uranus.revolution_animate()
#         # neptune.revolution_animate()
#         # print(RADIUS_MAP(SUN_RADIUS))
#
#         # esfera.revolution_animate()
#         # esfera.draw() #OK
#         # esfera.rotation(1,'y')  #OK
#
#
#         # triangulo.draw() #Ok
#         # triangulo.reflection() #OK
#         # triangulo.translation(1,0,0) #OK
#         # triangulo.rotation(1,'y') #OK
#
#
#
#
#         ENGINE.flip_and_clock(100)
#
