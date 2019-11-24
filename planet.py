
from shapes import *
import random
class CelestialObject():
    def __init__(self,radius,distance):
        self.radius = radius
        self.angle = 0
        self.distance = distance
        self.planets = []
        self.count = 0


    def spawnMoons(self,total):
        planets = []

        for x in range(total):
            r = self.radius*0.5
            d = random.randint(1,10)
            planets.append(CelestialObject(r,d))

        self.planets = planets


    def show(self):
        if self.count == 0:
            glTranslate(self.distance,0,0)
            glRotate(self.angle,0,0,0)
            self.count =+1

        Circle(0, 0, self.radius * 2, 4).draw()

        if self.planets:
            for planet in self.planets:
                planet.show()
