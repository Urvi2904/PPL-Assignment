#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Ellipse():
    def __init__(self, major_axis, minor_axis):
        self.a = major_axis
        self.b = minor_axis
        print("Ellipse formed")
    def getArea(self):
        return 3.14 * self.a * self.b
    def __del__(self):
        print("In destructor")


# In[44]:


class Circle(Ellipse):
    def __init__(self, a):
        self.radius = a
        print("Circle formed")
    def getArea(self):
        return 3.14 * self.radius * self.radius
    def getCircumference(self):
        return 2 * 3.14 * self.radius
    def __del__(self):
        print("In destructor")


# In[45]:


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
        p = self.per /2 
        return (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5
    def __del__(self):
        print("In destructor")


# In[46]:


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


# In[51]:


class Square():
    def __init__(self, side):
        self.n = 4
        self.length = side
    def getArea(self):
        return self.length * self.length
    def getPerimeter(self):
        return 4*self.length
    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
        return total / self.n
    def __del__(self):
        print("In destructor.")


# In[56]:


class Pentagon():
    def __init__(self, length):
        self.n = 5
        self.length = length
        print("Pentagon created.")
    def getArea(self):
        return (((5 * (5 + 2*(5**0.5))) ** 0.5) * (self.length ** 2)) / 4
    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
    def __del__(self):
        print("In destructor")


# In[57]:


class Hexagon():
    def __init__(self, length):
        self.n = 6
        self.length = length
        print("Hexagon created.")
    def getArea(self):
        return (3 * (3 ** 0.5) * (self.length ** 2)) / 2
    def angle(self):
        print("Angle between sides in degrees : ")
        total = 180 * (self.n - 2)
    def __del__(self):
        print("In destructor")


# In[58]:


import math
class Parallelogram():
    def __init__(self, length, breadth):
        self.n = 4
        self.length = length
        self.breadth = breadth
    def getAngle(self, angle):
        self.angle = math.radians(angle)
    def getPerimeter(self):
        return 2*(self.length + self.breadth)
    def getArea(self):
        return self.breadth * math.sin(self.angle) * self.length
    def __del__(self):
        print("In destructor")


# In[59]:


class Rhombus():
    def __init__(self, side):
        self.n = 4
        self.length = side
    def getAngle(self, angle):
        self.angle = math.radians(angle)
    def getArea(self):
        return self.breadth * math.sin(self.angle) * self.length
    def getPerimeter(self):
        return 4*self.length
    def __del__(self):
        print("In destructor")


# In[60]:


class EquiTriangle():
    def __init__(self, side):
        self.n = 3
        self.a = side
        print("Triangle created")
    def getPerimeter(self) :
        return 3*self.a
    def getArea(self):
        p = self.per
        return (3**0.5)*(self.a ** 2)/4
    def __del__(self):
        print("In destructor")

