def func(ls):
    """
    This function calculates the number of characters included in a given string
    
    Parameters:
    ls (str): given string
    
    Return:
    (int) - count of the symbols
    """
    return sum([1 for i in ls]) # whithout len(ls)

        
print(func("This function calculates the number of characters included in a given string"))