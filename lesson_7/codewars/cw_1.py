# Find The Distance Between Two Points
# https://www.codewars.com/kata/58b309e4bffc6b0a09000036

def distance(x1, y1, x2, y2):
    return round((((x1 - x2)**2 + (y1 - y2)**2)**0.5), 2)
