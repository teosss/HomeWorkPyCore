import super_module_t1

def input_area(value):
    """"
    This function determines the type of figure
    
    Input:
    value(str)
    
    Result:
    (int,float)
    """"
    if value is '1':
        s = int(input("Enter first side: "))
        b = int(input("Enter second side: "))
        return super_module_t1.rectangle_area(s,b)
    elif value is '2':
        s = int(input("Enter the base of the triangle: "))
        h = int(input("Enter the height of the triangle: "))
        return super_module_t1.triangle_area(s,h)
    elif value is '3': 
        r = int(input("Enter radius of circle: "))
        return super_module_t1.circle_area(r)
    else:
        value = input("You have entered incorrect data, please try again (1,2,3): ")
        return input_area(value)
    

value = input("The area of which figure you want to count: \n 1 - rectangle \n 2 - triangle \n 3 - circle \n Enter number: ")
print(input_area(value))