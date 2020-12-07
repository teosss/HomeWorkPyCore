login = input("Enter the login: ")

while True:
    if login == "First":
        print("Hello, ", login)
        break
    else:
        print("Invalid login. Please try again: ")
        login = input("!!!ERROR: Invalid login. \n Please, try again: ")
