# Basic subclasses - Adam and Eve
# https://www.codewars.com/kata/basic-subclasses-adam-and-eve

class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    Adam = Man()
    Eve = Woman()
    return [Adam, Eve]