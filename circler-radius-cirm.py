#2.The radius of a circle is 30 meters. Determine the area and circumference of the circle.
"""Area of a circle = pi*r(square)"""
"""Circumference of a circle = 2*pi*radius"""
pi = 3.14
radius = 30

def circle(area,circumference):
    area = pi*(radius**2)
    circumference = pi*2*radius
    return area, circumference;
print (circle(30,30))
