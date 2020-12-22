"""class Employee:
       '''Common base class for all employees'''
    emp_count = 0
   
    def init(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.emp_count += 1
   
    def displayCount(self):
       return f"Total Employee {Employee.emp_count}"
    def displayEmployee(self):
       return f"Name : {self.name},  Salary: {self.salary}"

#####################################
emp1 = Employee("Liubov", 350)
emp2 = Employee("Vasyl", 600)
emp3 = Employee("Liubomyr", 270)
#######################################
print(Employee.emp_count)
print(emp1.displayCount())
print(emp3.displayEmployee())
#########################################
print(f"Employee.doc:{Employee.__doc__}")
print(f"Employee.name:{Employee.__name__}")
print(f"Employee.module:{Employee.__module__}")
print(f"Employee.bases:{Employee.__bases__}")
print(f"Employee.dict:{Employee.__dict__}")"""

def check_odd_even(number):
    # n = int(input("Input entire number: "))
    while type(number) != int:
        try:
            number = int(number)
        except:
            print("You entered incorrect data. Please try again.")
            number = input("Input entire number:\n ")
    if number % 2 == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")

cheсk_odd_even(15)
# cheсk_odd_even(-6)
cheсk_odd_even("gth")
# cheсk_odd_even(0)