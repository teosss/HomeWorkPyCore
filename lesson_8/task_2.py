import re

def pass_validation():
    password = input("Please enter the password: ")
    if len(password) in range(6,16) and re.search(r'[0-9]', password) and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[$#@]', password) and not re.search(" ", password):
        return "Password  is valid"
    else: 
        print("Password is not valid, try again")
        return pass_validation()
            
print(pass_validation())