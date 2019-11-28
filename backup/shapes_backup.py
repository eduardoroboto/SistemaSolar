from OpenGL.GL import *
from math import sin, cos, pi, radians
import copy

from matrix import Matrix

# matematica de mapepamento
# Result := ((Input - InputLow) / (InputHigh - InputLow)) \
#          * (OutputHigh - OutputLow) + OutputLow;
def MAP(input, inputLow,inputHigh, outputLow ,outputHigh):
    """A simple function that take any number and scale it to a new number."""
    result = ((input - inputLow) / (inputHigh - inputLow)) * (outputHigh - outputLow) + outputLow

    return result



class Vertex():
    """A simple Class used to help on the logic of a Vertex on a OpenGL project"""

    def __init__(self, x, y,z=0):
        """Parameters
        ----------
        x : int
            Position on x axis
        y : int
            Position on y axis
        z : int, optional
            Position on z axis

        """

        self.x = x
        self.y = y
        self.z = z
       

    def get_point(self):
        """Function that convert x,y,z to a list"""

        return [self.x, self.y, self.z]


    def draw(self):
        """A draw Function that uses OpenGL to draw the Vertex"""

        glBegin(GL_POINTS)
        glColor((1, 1, 1))
        glVertex3fv(self.get_point())
        glEnd()

    def __to_matrix(self,type):
        """A Function that  convert the Vertex to a Matrix"""

        if type == 1:
            return  Matrix(4,1,[self.x,self.y,self.z,1])
        if type == 2:
            return Matrix(2,1, [self.x,self.y])
        if type == 3:
            return Matrix(3, 1, [self.x, self.y,self.z])
        if type == 4:
            return Matrix(3, 1, [self.x, self.y, 1])


    def __from_matrix(self, matriz):
        """A Function that  convert the a Matrix to Vertex"""

        self.x = matriz[1, 1]
        self.y = matriz[2, 1]
        self.z = matriz[3, 1]

    def update(self,x,y,z):
        """A Function that updates the parameters x,y,x """

        self.x = x
        self.y = y
        self.z = z


    def translation(self,dx,dy,dz=0):
        """A Function that makes the translation of the Vertex"""
        vertexMatrix = self.__to_matrix(1)

        translationMatrix = Matrix(4, 4, [1, 0, 0, dx, 0, 1, 0, dy, 0, 0, 1, dz, 0, 0, 0, 1])
        result = translationMatrix.dot(vertexMatrix)

        return self.__from_matrix(result)


    def rotation(self,angle,axis='z'):
        """A Function that makes the rotation of the Vertex based on angle and axis"""

        #angle = radians(angle)
        vertexMatrix = self.__to_matrix(3)

        a = 1 if axis == 'x' else 0
        b = 1 if axis == 'y' else 0
        c = 1 if axis == 'z' else 0


        OneMinusCosAngle = 1-cos(angle)

        x11 = ( cos(angle) + ( OneMinusCosAngle * (a**2) ) )
        x12 = ( OneMinusCosAngle * a * b + sin(angle) * c )
        x13 = ( OneMinusCosAngle * a * c - sin(angle) * b )
        x21 = ( OneMinusCosAngle * b * a - sin(angle) * c )
        x22 = ( cos(angle) + OneMinusCosAngle * ( b**2 ) )
        x23 = ( OneMinusCosAngle * b * c + sin(angle) * a )
        x31 = ( OneMinusCosAngle * c * a + sin(angle) * b )
        x32 = ( OneMinusCosAngle * c * b - sin(angle) * a )
        x33 = ( cos(angle) + OneMinusCosAngle* (c**2) )

        matrixRotation = Matrix(3,3,[x11,x12,x13,x21,x22,x23,x31,x32,x33])

        result = matrixRotation.dot(vertexMatrix)
        ok = result.return_list_cols(1)
        self.update(ok[0], ok[1], ok[2])

        # if len(xyz)==3:
        #     result = matrixRotation3dZ.dot(vertexMatrix)
        #     result = result.dot(vectorUnity)
        #     ok = result.return_list_cols(1)
        #     self.update(ok[0], ok[1], ok[2])







    def scale(self, dx, dy, dz=None):
        """A Function that makes the scale of the Vertex based on a new x,y,z"""


        if dz is not None:
            vertexMatrix = Matrix(1, 3,[self.x, self.y, self.z])

            scaleMatrix = Matrix(3,3 ,[dx,0,0,0,dy,0,0,0,dz])
            result = vertexMatrix.dot(scaleMatrix)
            ok = result.return_list_rows(1)
            self.update(ok[0], ok[1], ok[2])
        else:
            vertexMatrix = Matrix(1, 2,[self.x, self.y])
            scaleMatrix = Matrix(2,2, [dx,0,0,dy,])
            result =vertexMatrix.dot(scaleMatrix)
            ok = result.return_list_rows(1)
            self.update(ok[0],ok[1],0)

    def reflection(self,type):
        """A Function that makes the reflection of the Vertex with two types"""

        if type==1:
            vetexMatrix = self.__to_matrix(3)

            reflectionMatrix = Matrix(3,3, [1,0,0,0,-1,0,0,0,1])
            result = reflectionMatrix.dot(vetexMatrix)
            ok = result.return_list_cols(1)
            return ok
        elif type==2:
            vetexMatrix = self.__to_matrix(4)
            reflectionMatrix = Matrix(3, 3, [-1, 0, 0, 0, -1, 0, 0, 0, 1])
            result = reflectionMatrix.dot(vetexMatrix)
            ok = result.return_list_cols(1)
            return ok



    def projection(self):
        """A Function that makes the projection of the Vertex"""
        # TODO Fazer essa função projection no futuro para ficar legal no github.

        pass

    def shear(self,angle):
        """A Function that makes the shear of the Vertex"""
        # TODO Fazer essa função shear no futuro para ficar legal no github.


        pass

class Shape():

    """A simple Class used to help on using the Vertex functions of linear transformations
    on each Vertex of a Shape.
     """


    def translation(self, dx, dy, dz=0):
        for vertex in self.vertices:
            vertex.translation(dx,dy,dz)

    def rotation(self, angle,axis):
        for vertex in self.vertices:
            vertex.rotation(angle,axis)

    def scale(self, dx, dy, dz=None):
        for vertex in self.vertices:
            vertex.scale(dx, dy, dz)

    def reflection(self,type=1):
        reflection_vertices = list()
        for vertex in self.vertices:
            numbers = vertex.reflection(type)
            if len(numbers) == 2:
                reflection_vertices.append(Vertex(numbers[0],numbers[1]))
            else:
                reflection_vertices.append(Vertex(numbers[0],numbers[1],numbers[2]))

        self.draw(reflection_vertices)

    def projection(self):
        # TODO Fazer essa função projection no futuro para ficar legal no github.

        pass

    def shear(self, angle):
        # TODO Fazer essa função shear no futuro para ficar legal no github.

        pass


class Line(Shape):
    """ Class for the Line Shape """
    def __init__(self, x1, y1, z1, x2, y2,z2,color=(1,1,1)):
        self.line = [Vertex(x1, y1,z1), Vertex(x2, y2,z2)]
        self.color = color

    def draw(self,object=None):
        if object is None:
            glBegin(GL_LINES)
            glColor(self.color)
            for vertex in self.line:
                glVertex3fv(vertex.get_point())

            glEnd()
        else:
            glBegin(GL_LINES)
            glColor(self.color)
            for vertex in object.line:
                glVertex3fv(vertex.get_point())

            glEnd()



class Triangle(Shape):
    """ Class for the Triangle Shape """

    def __init__(self, a, b, c):
        self.vertices = self.__create_edges(a, b, c)

    def __create_edges(self, a, b, c):
        vertices_list = list()

        if type(a) is not Vertex and type(b) is not Vertex and type(c) is not Vertex:
            vertices_list.append(Vertex(a[0],a[1],a[2]))
            vertices_list.append(Vertex(b[0],b[1],b[2]))
            vertices_list.append(Vertex(c[0],c[1],c[2]))
        else:
            vertices_list.append(a)
            vertices_list.append(b)
            vertices_list.append(c)

        return vertices_list

    def draw(self,object=None):
        if object is None:
            glBegin(GL_TRIANGLES)
            glColor((0, 1, 0))
            for vertex in self.vertices:
                glVertex3fv(vertex.get_point())

            glEnd()
        else:
            glBegin(GL_TRIANGLES)
            glColor((0, 1, 0))
            for vertex in object:
                glVertex3fv(vertex.get_point())

            glEnd()


class Square(Shape):
    """ Class for the Square Shape """

    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.vertices = self.__create_vertices()

    def __create_vertices(self):
        vertices_list = list()

        vertices_list.append(Vertex(self.x, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y + self.width))
        vertices_list.append(Vertex(self.x, self.y + self.width))

        return vertices_list

    def draw(self,object=None):
        if object is None:
            glBegin(GL_TRIANGLES)

            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[2].get_point())

            glVertex3fv(self.vertices[2].get_point())
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[3].get_point())

            glEnd()
        else:
            glBegin(GL_TRIANGLES)

            glVertex3fv(object[0].get_point())
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[2].get_point())

            glVertex3fv(object[2].get_point())
            glVertex3fv(object[0].get_point())
            glVertex3fv(object[3].get_point())

            glEnd()



class Rectangle(Shape):
    """ Class for the Rectangle Shape """


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertices = self.__create_vertices()

    def __create_vertices(self):
        vertices_list = list()

        vertices_list.append(Vertex(self.x, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y + self.height))
        vertices_list.append(Vertex(self.x, self.y + self.height))

        return vertices_list

    def draw(self, object=None):
        if object is None:
            glBegin(GL_TRIANGLES)

            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[2].get_point())

            glVertex3fv(self.vertices[2].get_point())
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[3].get_point())

            glEnd()
        else:
            glBegin(GL_TRIANGLES)

            glVertex3fv(object[0].get_point())
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[2].get_point())

            glVertex3fv(object[2].get_point())
            glVertex3fv(object[0].get_point())
            glVertex3fv(object[3].get_point())

            glEnd()


class Circle(Shape):
    """ Class for the Circle Shape """


    def __init__(self, x, y, radius, number):
        self.x = x
        self.y = y
        self.radius = radius
        self.number = number

        self.vertices = self.__create_edges(self.x, self.y, self.radius,self.number)

    def __create_edges(self, x, y, radius,number):
        vertices_list = list()

        hx = copy.copy(x)
        hy = copy.copy(y)
        angle = 2*pi / number
        for i in range(0, number):
            vertices_list.append(Vertex(hx, hy))
            x = hx+radius * cos(i*angle)
            y =  hy+radius * sin(i*angle)
            vertices_list.append(Vertex(x, y))
            x2 = hx+radius * cos((i+1)*angle)
            y2 = hy+radius * sin((i+1)*angle)
            vertices_list.append(Vertex(x2 , y2))


        return vertices_list


    def draw(self,object=None):
        if object is None:
            glBegin(GL_TRIANGLES)
            glColor4fv((1, 1, 1,1))
            color = 0

            for vertex in self.vertices:
                glVertex3fv(vertex.get_point())

            glEnd()
        else:
            glBegin(GL_TRIANGLES)
            glColor4fv((1, 1, 1, 1))
            color = 0

            for vertex in object:
                glVertex3fv(vertex.get_point())

            glEnd()


class Cube(Shape):
    """ Class for the Cube Shape """

    def __init__(self,x,y,z,width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width

        self.vertices = self.__create_edges(self.x,self.y,self.z,self.width)

    def __create_edges(self, x, y,z, width):
        vertices_list = list()

        vertices_list.append(Vertex(x, y, z))
        vertices_list.append(Vertex(x + width, y,z))
        vertices_list.append(Vertex(x + width, y + width,z))
        vertices_list.append(Vertex(x, y + width,z))

        vertices_list.append(Vertex(x, y, z+width))
        vertices_list.append(Vertex(x + width, y, z+width))
        vertices_list.append(Vertex(x + width, y + width, z+width))
        vertices_list.append(Vertex(x, y + width, z+width))

        return vertices_list

    def draw(self,object=None):
        if object is None:
            glBegin(GL_TRIANGLES)
            #glColor((0, 1, 0))
            #lado 1
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[2].get_point())

            glVertex3fv(self.vertices[2].get_point())
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[3].get_point())
            #lado 2
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[4].get_point())
            glVertex3fv(self.vertices[7].get_point())

            glVertex3fv(self.vertices[7].get_point())
            glVertex3fv(self.vertices[0].get_point())
            glVertex3fv(self.vertices[3].get_point())

            #lado 3

            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[5].get_point())
            glVertex3fv(self.vertices[6].get_point())

            glVertex3fv(self.vertices[6].get_point())
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[2].get_point())

            #lado 4
            glVertex3fv(self.vertices[2].get_point())
            glVertex3fv(self.vertices[6].get_point())
            glVertex3fv(self.vertices[7].get_point())

            glVertex3fv(self.vertices[7].get_point())
            glVertex3fv(self.vertices[2].get_point())
            glVertex3fv(self.vertices[3].get_point())

            # lado 5
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[5].get_point())
            glVertex3fv(self.vertices[4].get_point())

            glVertex3fv(self.vertices[4].get_point())
            glVertex3fv(self.vertices[1].get_point())
            glVertex3fv(self.vertices[0].get_point())

            # lado 6
            glVertex3fv(self.vertices[4].get_point())
            glVertex3fv(self.vertices[5].get_point())
            glVertex3fv(self.vertices[6].get_point())

            glVertex3fv(self.vertices[6].get_point())
            glVertex3fv(self.vertices[4].get_point())
            glVertex3fv(self.vertices[7].get_point())

            glEnd()

        else:
            glBegin(GL_TRIANGLES)

            glVertex3fv(object[0].get_point())
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[2].get_point())

            glVertex3fv(object[2].get_point())
            glVertex3fv(object[0].get_point())
            glVertex3fv(object[3].get_point())
            # lado 2
            glVertex3fv(object[0].get_point())
            glVertex3fv(object[4].get_point())
            glVertex3fv(object[7].get_point())

            glVertex3fv(object[7].get_point())
            glVertex3fv(object[0].get_point())
            glVertex3fv(object[3].get_point())

            # lado 3

            glVertex3fv(object[1].get_point())
            glVertex3fv(object[5].get_point())
            glVertex3fv(object[6].get_point())

            glVertex3fv(object[6].get_point())
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[2].get_point())

            # lado 4
            glVertex3fv(object[2].get_point())
            glVertex3fv(object[6].get_point())
            glVertex3fv(object[7].get_point())

            glVertex3fv(object[7].get_point())
            glVertex3fv(object[2].get_point())
            glVertex3fv(object[3].get_point())

            # lado 5
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[5].get_point())
            glVertex3fv(object[4].get_point())

            glVertex3fv(object[4].get_point())
            glVertex3fv(object[1].get_point())
            glVertex3fv(object[0].get_point())

            # lado 6
            glVertex3fv(object[4].get_point())
            glVertex3fv(object[5].get_point())
            glVertex3fv(object[6].get_point())

            glVertex3fv(object[6].get_point())
            glVertex3fv(object[4].get_point())
            glVertex3fv(object[7].get_point())

            glEnd()

class Cuboid(Shape):
    """ Class for the Cuboid Shape """

    def __init__(self,x,y,z,width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height

        self.vertices = self.__create_vertices(x,y,z,width,height)

    def __create_vertices(self,x,y,z,width,height):
        points_list = list()

        points_list.append((x, y, z))
        points_list.append((x + width, y, z))
        points_list.append((x + width, y + width, z))
        points_list.append((x, y + width, z))

        points_list.append((self.x, self.y))
        points_list.append((self.x + self.width, self.y))
        points_list.append((self.x + self.width, self.y + self.height))
        points_list.append((self.x, self.y + self.height))

        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[1])
        glVertex3fv(self.vertices[2])

        glVertex3fv(self.vertices[2])
        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[3])

        glEnd()




class Sphere(Shape):
    """ Class for the Sphere Shape """

    def __init__(self,x,y,z,radius,total):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.total = total
        self.halfPI = pi / 2

        self.vertices = self.__creat_vertices(self.x,self.y,self.z)




    def __creat_vertices(self,x,y,z):
        globe = Matrix(self.total+1,self.total+1)

        for i in range(self.total+1):
            lon = MAP(i, 0, self.total,-pi,pi)
            for j in range(self.total+1):
                lat = MAP(j, 0, self.total, -self.halfPI, self.halfPI)
                xC = self.radius * sin(lon) * cos(lat)
                yC = self.radius * sin(lon) * sin(lat)
                zC = self.radius * cos(lon)
                globe[i,j] = Vertex(xC+x, yC+y, zC+z)

        return globe


    #GL_TRIANGLE_STRIP
    def draw(self,object=None):
        if object is None:
            glBegin(GL_TRIANGLE_STRIP)
            glColor4fv((0, 0, 1,0.3))
            for i in range(self.total+1):
                for j in range(self.total+1):
                    glVertex3fv(self.vertices[i,j].get_point())
                    glVertex3fv(self.vertices[i+1,j].get_point())

            glEnd()
        else:
            glBegin(GL_TRIANGLE_STRIP)
            glColor4fv((0, 0, 1, 0.3))
            for i in range(self.total):
                for j in range(self.total + 1):
                    glVertex3fv(object[i, j].get_point())
                    glVertex3fv(object[i + 1, j].get_point())

            glEnd()


    def translation(self, dx, dy, dz=None):
        if dz is not None:
            for i in range(self.total+1):
                for j in range(self.total + 1):
                    self.vertices[i,j].translation(dx,dy,dz)
                    self.vertices[i+1, j].translation(dx, dy, dz)
        else:
            for i in range(self.total):
                for j in range(self.total + 1):
                    self.vertices[i,j].translation(dx,dy,0)
                    self.vertices[i + 1, j].translation(dx, dy, 0)

    def rotation(self, angle,axis='z'):
        for i in range(self.total+1):
            for j in range(self.total + 1):
                self.vertices[i,j].rotation(angle, axis)



    def reflection(self, type=1):
        if type == 1:
            vetexMatrix = Matrix(3, 1, [self.x, self.y,self.z])

            reflectionMatrix = Matrix(3, 3, [1, 0, 0, 0, -1, 0, 0, 0, 1])
            result = reflectionMatrix.dot(vetexMatrix)
            ok = result.return_list_cols(1)

            reflectioGlobe = self.__creat_vertices(ok[0],ok[1],ok[2])

        elif type == 2:
            vetexMatrix = Matrix(3, 1, [self.x, self.y,self.z])
            reflectionMatrix = Matrix(3, 3, [-1, 0, 0, 0, -1, 0, 0, 0, 1])
            result = reflectionMatrix.dot(vetexMatrix)
            ok = result.return_list_cols(1)

            reflectioGlobe = self.__creat_vertices(ok[0],ok[1],ok[2])

        self.draw(reflectioGlobe)










class Pyramid(Shape):
    """ Class for the Pyramid Shape """

    def __init__(self, x, y, z,width, heigth):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = heigth
        self.high_point = Vertex(x+(width/2),y+(width/2),z-(width/2))
        self.vertices = self.__create_triangles()

    def __create_triangles(self):
        list = []
        high = self.high_point
        # primeiro triangulo
        a = Vertex(self.x, self.y, self.z)
        b = Vertex(self.x + self.width, self.y, self.z)
        c = Vertex(self.x + self.width, self.y , self.z- self.width)
        list.append(Triangle(a, b, c))
        # segundo triangulo
        c = Vertex(self.x + self.width, self.y, self.z- self.width)
        d = Vertex(self.x, self.y, self.z - self.width)
        a = Vertex(self.x, self.y, self.z)
        list.append(Triangle(c, d, a))
        list.append(Triangle(a, high, b))
        list.append(Triangle(b, high, c))
        list.append(Triangle(c, high, d))
        list.append(Triangle(d, high, a))

        return list
    def draw(self,object=None):
        if object is None:
            for tri in self.vertices:
                tri.draw()
        else:
            for tri in object:
                tri.draw()