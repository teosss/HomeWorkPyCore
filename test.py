def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pum <= fuel_left * mpg:
        return True
    else:
        return False

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))