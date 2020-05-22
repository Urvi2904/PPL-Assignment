#!/usr/bin/env python
# coding: utf-8

# # Inheritance

# In[1]:


import turtle


# In[2]:


class Ellipse():
    def __init__(self, major_axis, minor_axis):
        self.a = major_axis
        self.b = minor_axis
        print("Ellipse formed")
    def getArea(self):
        return 3.14 * self.a * self.b
    def draw(self):
        turtle.shape("circle")
        turtle.shapesize(self.b, self.a,1)
        turtle.fillcolor("white")
        turtle.mainloop()
    def __del__(self):
        print("In destructor")


# In[3]:


class Circle(Ellipse):
    def __init__(self, a):
        self.a = self.b = a
        print("Circle formed")
    def draw(self):
        turtle.circle(self.a)
        #turtle.shapesize(3,5,1)
        turtle.fillcolor("white")
        turtle.mainloop()
    def getCircumference(self):
        return 2 * 3.14 * self.a


# In[4]:


e = Ellipse(30, 10)


# In[5]:


e.draw()


# In[6]:


c =  Circle(100)


# In[8]:


c.draw()


# In[6]:


c.getCircumference()


# ## Encapsulation

# In[9]:


class Ellipse():
    def __init__(self, major_axis, minor_axis):
        self.__a = major_axis
        self.__b = minor_axis
        print("Ellipse formed")
    def getArea(self):
        return 3.14 * self.__a * self.__b
    def __del__(self):
        print("In destructor")


# In[10]:


class Circle(Ellipse):
    def __init__(self, a):
        self.__a = self.__b = a
        print("Circle formed")
    def getCircumference(self):
        return 2 * 3.14 * self.__a


# In[11]:


c2 = Circle(7)


# In[12]:


c2.getArea()


# In[20]:


del c1


# In[21]:


c1.getCircumference()


# ## Polygons : Encapsulation and Abstraction

# In[13]:


class RegularPolygon():
    def __init__(self, sides, length):
        self.n = sides
        self.length = length
    def __angle(self):
        print("Angle between sides in degrees : ")
        self.total = 180 * (self.n - 2)
        return self.total / self.n
    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        self.an = total / self.n
        return self.an
    def getPerimeter(self) :
        return  self.length * self.n
    def __del__(self) :
        print("In destructor")


# In[14]:


class EquiTriangle(RegularPolygon):
    def __init__(self, length):
        self.n = 3
        self.length = length
        print("Triangle created")
    def getArea(self):
        return (3 ** 0.5) * (self.length ** 2)


# In[15]:


et = EquiTriangle(4)


# In[16]:


et.__angle()


# In[17]:


et.angle()


# In[138]:


class Triangle():
    def __init__(self, side1, side2, side3):
        self.n = 3
        self.a = side1
        self.b = side2
        self.c = side3
        print("Triangle created")
    def getPerimeter(self) :
        self.per = self.a + self.b + self.c
        return self.per
    def getArea(self):
        p = self.per / 2
        return (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5


# In[18]:


class Rectangle():
    def __init__(self, length, breadth):
        self.n = 4
        self.length = length
        self.breadth = breadth
        print("Rectangle formed")
    def getArea(self):
        return self.length * self.breadth
    def getPerimeter(self):
        return 2*(self.length + self.breadth)
    def __del__(self):
        print("In destructor.")


# In[19]:


class Square(Rectangle, RegularPolygon):
    def __init__(self, length):
        self.n = 4
        self.length = length
        self.breadth = length
        print("4 sided polygon")


# In[20]:


class Pentagon(RegularPolygon):
    def __init__(self, length):
        self.n = 5
        self.length = length
        print("Pentagon created.")
    def getArea(self):
        return (((5 * (5 + 2*(5**0.5))) ** 0.5) * (self.length ** 2)) / 4


# In[21]:


class Hexagon(RegularPolygon):
    def __init__(self, length):
        self.n = 6
        self.length = length
        print("Hexagon created.")
    def getArea(self):
        return (3 * (3 ** 0.5) * (self.length ** 2)) / 2


# In[22]:


import math
class Parallelogram(Rectangle):
    def getAngle(self, angle):
        self.angle = math.radians(angle)
    def getArea(self):
        return self.breadth * math.sin(self.angle) * self.length


# In[23]:


class Rhombus(Square, Parallelogram):
    def print(self):
        print("In rhombus")


# In[24]:


r1 = Rhombus(5)


# In[ ]:




