# Create a simple generator function similar to the range iterator.

def sg_to_ri(start = 0, stop = 0):
        if start > stop:
            start, stop = stop, start
        while start < stop:
            yield start
            start += 1
            
temp = sg_to_ri(2,8)
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))
print(next(temp))

"""
Через ітератор

class IteratorRange():
    def __init__(self, start = 0, stop = 0):
        if start > stop:
            self.start = stop
            self.stop = start
        else:
            self.start = start
            self.stop = stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

myclass = IteratorRange(5,9)
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""

    