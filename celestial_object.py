from shapes import Sphere, Vertex
from OpenGL.GL import *
from math import sin, cos, pi, radians
import copy


class CelestialObject():
    def __init__(self,x,y,z,radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.total = 10
        self.globe = Sphere(self.x,self.y,self.z,self.radius, self.total)
        self.more = dict()

        self.vertices_list = []
        self.number_revolution=0
        self.revolution_loop=0

    def sun_revolution(self, x, y, radius, number=60):
        # cc = Circle(1,1,radius,number)
        # cc.draw()
        hx = copy.copy(x)
        hy = copy.copy(y)
        angle = 2 * pi / number
        for i in range(0, number):
            # vertices_list.append(Vertex(hx, hy))
            x = hx + radius * cos(i * angle)
            y = hy + radius * sin(i * angle)
            self.vertices_list.append(Vertex(x, y))

        self.number_revolution = len(self.vertices_list)


    def moon_revolution(self, list_of_points, radius ,number=60):
        for i in range(len(list_of_points)):
            hx = copy.copy(list_of_points[i].x)
            hy = copy.copy(list_of_points[i].y)
            angle = 2 * pi / number
            x = hx + radius * cos(i * angle)
            y = hy + radius * sin(i * angle)
            self.vertices_list.append(Vertex(x, y))

        self.number_revolution = len(self.vertices_list)



    def revolution_animate(self):
        if self.revolution_loop == self.number_revolution:
            self.revolution_loop = 0
        x = self.vertices_list[self.revolution_loop].x
        y = self.vertices_list[self.revolution_loop].y
        z = self.vertices_list[self.revolution_loop].z

        Sphere(x,y,z ,self.radius, self.total).draw()
        self.revolution_loop += 1

        print(self.revolution_loop , self.number_revolution)

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