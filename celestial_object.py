from shapes import Sphere, Vertex, Line, Circle
from math import pi,cos, atan,sin,tan
from global_variables import DISTANCE_MAP
import copy



class CelestialObject():
    """A Class used to create and animate Celestial Objects using the object Sphere from shapes file"""

    def __init__(self,radius,color):
        """Parameters
               ----------
               radius : int
                   Radius of Sphere.
               color : Tuple (Int,Int,Int)
                   Tuple with RGB color from 0 to 1.
               ----------
            Helper Variables
                orbit_list : int
                    Total of verticies of the Orbit.
                __total : int
                    Total of Polygons for the Sphere shapes.
               __mode : String
                    3D or 2D vizualization.
               __number_revolution : int
                    Size of orbit_list
               __revolution_loop : int
                    Position on orbit list for animation
               """

        self.radius = radius
        self.color = color
        self.orbit_list = []

        self.__total = 10
        self.__mode = '3D'
        self.__number_revolution=0
        self.__revolution_loop=0

    def sun_revolution(self,radius,orbital_period,eccentricity, number):
        """Function that generates the moviment of Object on a Start"""

        angles = self.__make_kepler_orbit(eccentricity,orbital_period,number)
        semimajor_axis = self.__keplerIII_period_to_semimajor_axis(orbital_period)
        xOrbit, yOrbit = self.__orbit(semimajor_axis, eccentricity, angles)

        for i in range(0, number):
            print("X Y Keppler ",xOrbit[i], yOrbit[i])
            x =  DISTANCE_MAP(xOrbit[i])
            y =  DISTANCE_MAP(yOrbit[i])
            self.orbit_list.append(Vertex(x, y))

        self.__number_revolution = len(self.orbit_list)

    def moon_revolution(self, list_of_points, radius ,number=60):
        """Function that generates the moviment of Object on a Planet"""

        points = list_of_points+list_of_points
        for i in range(len(points)):
            hx = copy.copy(points[i].x)
            hy = copy.copy(points[i].y)
            angle = 2 * pi / number
            x = hx + radius * cos(i * angle)
            y = hy + radius * sin(i * angle)
            self.orbit_list.append(Vertex(x, y))

        self.__number_revolution = len(self.orbit_list)


    def revolution_animate(self, ring='n'):
        """Function that makes the animation of moviment"""

        if ring == 'y':
            self.draw_ring()

        if self.__revolution_loop == self.__number_revolution:
            self.__revolution_loop = 0
        x = self.orbit_list[self.__revolution_loop].x
        y = self.orbit_list[self.__revolution_loop].y
        z = self.orbit_list[self.__revolution_loop].z

        if self.__mode == "2D":
            Circle(x,y ,self.radius, self.__total).draw()


        else:
            Sphere(x,y,z ,self.radius, self.__total,self.color).draw()

        self.__revolution_loop += 1

    def draw_ring(self):
        """Function that draws a line on the Orbit following the Planet"""

        for i in range(1,self.__revolution_loop):
            x1 = self.orbit_list[i].x
            y1 = self.orbit_list[i].y
            x2 = self.orbit_list[i-1].x
            y2 = self.orbit_list[i-1].y
            Line(x1,y1,0,x2,y2,0,).draw()
    def draw_ringAll(self):
        """Function that draws a line on the Orbit"""

        for i in range(1,len(self.orbit_list)):
            x1 = self.orbit_list[i].x
            y1 = self.orbit_list[i].y
            x2 = self.orbit_list[i-1].x
            y2 = self.orbit_list[i-1].y
            Line(x1,y1,0,x2,y2,0,).draw()

    def draw(self):
        if self.__mode == "2D":
            Circle(0,0,  self.radius, self.__total).draw()
        else:
            Sphere(0,0,0,self.radius, self.__total,self.color).draw()

    def __keplerIII_period_to_semimajor_axis(self,orbital_period):
        """Function that convert the  orbital_period to semimajor_axis"""

        semimajor_axis_cubed = orbital_period ** 2
        semimajor_axis = semimajor_axis_cubed ** (1. / 3.)

        return semimajor_axis

    def __make_kepler_orbit(self,eccentricity, orbital_period, nStep):
        """Function that gets the eccentricity, orbital_period and Steps to return a list of Angles"""

        lower = 0.0
        upper = orbital_period
        length = nStep
        tRange = [lower + x * (upper - lower) / (length - 1) for x in range(length)]

        theta = []
        for time in tRange:
            PsiDiff = 1.0
            M = 2 * pi * time / orbital_period
            PsiOld = M
            while PsiDiff > 1e-10:
                PsiNew = M + eccentricity * sin(PsiOld)
                PsiDiff = PsiNew - PsiOld
                PsiOld = PsiNew
            theta0 = 2 * atan(((1 + eccentricity) / (1 - eccentricity)) ** (0.5) * tan(PsiOld / 2.))
            theta.append(theta0)
        return theta

    def __orbit(self, semimajor_axis, eccentricity, true_anomaly_list):
        """Function that gets the semimajor_axis, eccentricity and List of Angles to a return a list of Vertex with X, Y, Z"""
        x_orbit = []
        y_orbit = []
        # define the shape equation
        for true_anomaly in true_anomaly_list:
            r_orbit = semimajor_axis * (1 - eccentricity ** 2) / (1 + eccentricity * cos(true_anomaly))
            x_orbit.append(r_orbit * cos(true_anomaly))
            y_orbit.append(r_orbit * sin(true_anomaly))

        return x_orbit, y_orbit


class Planet(CelestialObject):
    """ Planet Class"""
    pass

class Star(CelestialObject):
    """ Star Class"""

    pass

class Moon(CelestialObject):
    """ Moon Class"""
    def __init__(self,radius,color):
        if radius < 0.01:
            super().__init__(radius*100,color)
        else:
            super().__init__(radius,color)

