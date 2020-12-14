from math import pi

def rectangle(*side):
    """
    This function calculates the square of rectangle
    
    Parameters:
    a (float), b (float): the sides of the rectangle
    
    Returns:
    (float)
    """
    return sum(side)
    
def triangle(*side):
    """
    This function calculates the square of triangle
    
    Parameters:
    a (float), b (float), c (float): the sides of the rectangle
    
    Returns:
    (float)
    """
    return sum(side)

def circle(r):
    """
    This function calculates the square of circle
    
    Parameters:
    r (float) - radius of the circle
    
    Returns:
    (float)
    """ 
    
    return 2*pi*r

parameter = input("Enter the number of which shape you want to find the perimeter: \n 1 if rectangle \n 2 if triangle \n 3 if circle \n Enter number: ")
if parameter == "1":
    a = float(input("Side 1 = "))
    b = float(input("Side 2 = "))
    print("Square of rectangle is {}".format(rectangle(a,b))) 
elif parameter == "2":
    a = float(input("Side 1 = "))
    b = float(input("Side 2 = "))
    c = float(input("Side 3 = "))
    print("Square of triangle is {}".format(triangle(a,b,c)))
elif parameter == "3":
    r = float(input("Radius = ")) 
    print("Square of circle is {:.3f}".format(circle(r)))     