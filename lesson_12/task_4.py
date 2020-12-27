def miles1(km):
    return list(map(lambda item: 1.6*item, km))

def miles2(km):
    km = [item*1.6 for item in km]
    return km

km = [4, 5, 6, 8, 1, 5]
print(miles1(km))
print(miles2(km))