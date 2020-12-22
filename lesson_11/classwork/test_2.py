number = input("Enter nuber 1,2: ")
a, b = number.split(",")
try: 
    a = int(a)
    b = int(b)
    
    result = a / b
    print(result)  

except ValueError as e:
    print("Please enter correct number. ", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError!")  
else:
    print("Else1 of exception")
finally:
    print("End of exception")
    
  
    
    
