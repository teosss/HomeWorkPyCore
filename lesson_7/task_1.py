def LARGEST_NUMBER(arg1,arg2):
    """
    This function finds the largest number in two parameter
    
    Parameters:
    arg1(int or float)
    arg2(int or float) 
    
    Returns:
    Largest number 
    """
    return arg1 if arg1 > arg2 else arg2

print(LARGEST_NUMBER(121,311))
print(LARGEST_NUMBER.__doc__)