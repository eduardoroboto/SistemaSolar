from shapes import Sphere, Vertex
from OpenGL.GL import *
from math import sin, cos, pi, radians
import copy


class CelestialObject():
    def __init__(self,x,y,z,radius,gravity):
        self.x = x
        self.y = y
        self.z = z
        self.gravity = gravity
        self.radius = radius
        self.total = 20
        self.globe = Sphere(self.x,self.y,self.z,self.radius, self.total)
        self.more = dict()

        self.all_globes=None
        self.number_revolution=0
        self.revolution_loop=0

    def revolution_generate(self, x, y, radius, number=60):
        # cc = Circle(1,1,radius,number)
        # cc.draw()

        vertices_list = list()

        hx = copy.copy(x)
        hy = copy.copy(y)
        angle = 2 * pi / number
        for i in range(0, number):
            # vertices_list.append(Vertex(hx, hy))
            x = hx + radius * cos(i * angle)
            y = hy + radius * sin(i * angle)
            vertices_list.append(Vertex(x, y))

        list_of_globes = list()
        for vtx in vertices_list:
            print(vtx)
            # def __init__(self, x, y, z, radius, total):
            gg = Sphere(vtx.x, vtx.y, vtx.z, self.radius, self.total)
            list_of_globes.append(gg)

        self.number_revolution = len(list_of_globes)
        self.all_globes = list_of_globes

    def revolution_animate(self):
        print(self.revolution_loop)
        if self.revolution_loop == self.number_revolution:
            self.revolution_loop = 0
        print(self.revolution_loop)
        print(self.number_revolution)
        print(self.all_globes[self.revolution_loop])
        self.all_globes[self.revolution_loop].draw()

        self.revolution_loop += 1

    def rotation(self):
        pass

    def draw(self):
        self.globe.draw()

class Planet(CelestialObject):
    def __int__(self,x,y,z,radius,gravity):
        super().__init__(x,y,z,radius,gravity)

class Star(CelestialObject):
    def __int__(self,x,y,z,radius,gravity):
        super().__init__(x, y, z,radius,gravity)

class Universe():
    pass

class Gravity():
    pass

class SolarSystem():
    def __int__(self):
        pass