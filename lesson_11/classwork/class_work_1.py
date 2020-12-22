class Car:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model
    
    def start(self):
        print (f"Car {self.name} starts")
    
    def stop(self):
        print (f"Car {self.name} stop")
 
     
class Human:
    species = "Homosapience"
    
    def __init__(self, name):
        self.name = name 
    
    def whoyouare(self):
        self.classmethod()
        self.staticmethod()
        return f"You name is {self.name}"
    
    @classmethod
    def classmethod(cls):
        print(f"You are {cls.species}")       
    
    @staticmethod
    def staticmethod():  
        print("Hi human")


viktor = Human("Viktor")

viktor.whoyouare()

class Employee:
    employee_counter = 0
    
    def __init__(self, x, name, salary):
        
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1
    
    def __get_name(self):    
        return self.name
    
    def __get_salary(self):
        return self.salary

        
    x = property(__get_name, __get_salary)

emp1 = Employee("Liubov", 350)
emp2 = Employee("Vasyl", 600)
emp3 = Employee("Liubomyr", 270)