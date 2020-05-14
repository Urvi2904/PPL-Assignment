#!/usr/bin/env python
# coding: utf-8

# # Inheritance

# In[109]:


class Ellipse():
    def __init__(self, major_axis, minor_axis):
        self.a = major_axis
        self.b = minor_axis
        print("Ellipse formed")
    def getArea(self):
        return 3.14 * self.a * self.b
    def __del__(self):
        print("In destructor")


# In[110]:


class Circle(Ellipse):
    def __init__(self, a):
        self.a = self.b = a
        print("Circle formed")
    def getCircumference(self):
        return 2 * 3.14 * self.a


# In[114]:


class RegularPolygon():
    def __init__(self, sides, length):
        self.n = sides
        self.length = length
    def angle(self):
        print("Angle between sides in degrees : ")
        self.total = 180 * (self.n - 2)
        return self.total / self.n
    def getPerimeter(self) :
        return  self.length * self.n
    def __del_(self) :
            print("In destructor")


# In[115]:


class EquiTriangle(RegularPolygon):
    def __init__(self, length):
        self.n = 3
        self.length = length
        print("Triangle created")
    def getArea(self):
        return (3 ** 0.5) * (self.length ** 2)


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


# In[147]:


class Rectangle():
    def __init__(self, length, breadth):
        self.n = 4
        self.length = length
        self.breadth = breadth
    def getArea(self):
        return self.length * self.breadth
    def getPerimeter(self):
        return 2*(self.length + self.breadth)
    def __del__(self):
        print("In destructor.")


# In[151]:


class Square(Rectangle, RegularPolygon):
    def __init__(self, length):
        self.n = 4
        self.length = length
        self.breadth = length


# In[158]:


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


# In[159]:


import math
class Parallelogram(Rectangle):
    def getAngle(self, angle):
        self.angle = math.radians(angle)
    def getArea(self):
        return self.breadth * math.sin(self.angle) * self.length


# In[162]:


class Rhombus(Square, Parallelogram):
    def print(self):
        print("In rhombus")


# In[ ]:




