from math import pow
from math import pi

def triangle_area(s,h):
    return 0.5*h*s
    
def rectangle_area(s,b):
    return s*b
    
def circle_area(r):
    return round(pi*pow(r,2),2)