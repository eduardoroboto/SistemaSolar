from shapes import Sphere, Vertex, Line, Circle
from OpenGL.GL import *
from math import *
from global_variables import *
import copy
import sys
import pygame
from pygame.locals import *



class CelestialObject():
    def __init__(self,radius,color):
        self.radius = radius
        self.total = 10
        self.more = dict()
        self.mode = '3D'
        self.color = color

        self.vertices_list = []
        self.number_revolution=0
        self.revolution_loop=0

    # def sun_revolutionnnnn(self,radius, number=60):
    #     # cc = Circle(1,1,radius,number)
    #     # cc.draw()
    #     angle = 2 * pi / number
    #     for i in range(0, number):
    #         # vertices_list.append(Vertex(hx, hy))
    #         x = radius * cos(i * angle)
    #         y = radius * sin(i * angle)
    #         print("X Y Circle", x,y)
    #         self.vertices_list.append(Vertex(x, y))
    #
    #     self.number_revolution = len(self.vertices_list)

    def sun_revolution(self,radius,orbital_period,eccentricity, number):
        # cc = Circle(1,1,radius,number)
        # cc.draw()
        angles = make_kepler_orbit(eccentricity,orbital_period,number)
        semimajor_axis = keplerIII_period_to_semimajor_axis(orbital_period)
        xOrbit, yOrbit = orbit(radius,semimajor_axis, eccentricity, angles)

        for i in range(0, number):
            print("X Y Keppler ",xOrbit[i], yOrbit[i])
            x =  DISTANCE_MAP(xOrbit[i])
            y =  DISTANCE_MAP(yOrbit[i])
            self.vertices_list.append(Vertex(x, y))

        self.number_revolution = len(self.vertices_list)

    def moon_revolution(self, list_of_points, radius ,number=60):
        points = list_of_points+list_of_points
        for i in range(len(points)):
            hx = copy.copy(points[i].x)
            hy = copy.copy(points[i].y)
            angle = 2 * pi / number
            x = hx + radius * cos(i * angle)
            y = hy + radius * sin(i * angle)
            self.vertices_list.append(Vertex(x, y))

        self.number_revolution = len(self.vertices_list)




    def revolution_animate(self, ring='n',camera='n'):
        if ring == 'y':
            self.draw_ring()

        if self.revolution_loop == self.number_revolution:
            self.revolution_loop = 0
        x = self.vertices_list[self.revolution_loop].x
        y = self.vertices_list[self.revolution_loop].y
        z = self.vertices_list[self.revolution_loop].z

        if self.mode == "2D":
            Circle(x,y ,self.radius, self.total,self.color).draw()


        else:
            Sphere(x,y,z ,self.radius, self.total,self.color).draw()

        self.revolution_loop += 1

        # print(self.revolution_loop , self.number_revolution)

    def draw_ring(self):
        for i in range(1,self.revolution_loop):
            x1 = self.vertices_list[i].x
            y1 = self.vertices_list[i].y
            x2 = self.vertices_list[i-1].x
            y2 = self.vertices_list[i-1].y
            Line(x1,y1,0,x2,y2,0,).draw()
    def draw_ringAll(self):
        for i in range(1,len(self.vertices_list)):
            x1 = self.vertices_list[i].x
            y1 = self.vertices_list[i].y
            x2 = self.vertices_list[i-1].x
            y2 = self.vertices_list[i-1].y
            Line(x1,y1,0,x2,y2,0,).draw()

    def draw(self):
        if self.mode == "2D":
            Circle(0,0,  self.radius, self.total).draw()
        else:
            Sphere(0,0,0,self.radius, self.total,self.color).draw()

class Planet(CelestialObject):
    pass

class Star(CelestialObject):
    pass

class Moon(CelestialObject):

    def __init__(self,radius,color):
        if radius < 0.01:
            super().__init__(radius*100,color)
        else:
            super().__init__(radius,color)

