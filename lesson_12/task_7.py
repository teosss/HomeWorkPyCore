#Using several decorators, create a sandwich consisting of lettuce, tomatoes and meat. 
#<\ ^^^^^^^ /> 
# tomato # 
#-meat– 
#~ salad ~
# <\ ______ />


def sandwich(func):
    def inner(*args, **kwargs):
        print("<\ ^^^^^^^ />")
        func(*args, **kwargs)
        print("<\ ______ />")
    return inner


@sandwich
def products(ls):
    print(f"# {ls[0]} #")
    print(f"-- {ls[1]} --")     
    print(f"~ {ls[2]} ~")     

products(["tomato", "meat", "salad"])