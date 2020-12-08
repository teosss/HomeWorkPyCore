even = []
odd = []
div23 = []
for i in range(1,10):
    if i % 2 == 0:
        even.append(i)
    if i % 3 == 0:
        odd.append(i)
    if i % 2 != 0 and i % 3 != 0:
        div23.append(i)

print("Even numbers: ", even)
print("Odd numbers: ", odd)
print("Numbers div 2 and 3: ", div23)

print()

print("Even numbers: ", list(i for i in range(1,10) if i % 2 == 0))
print("Odd numbers: ", list(i for i in range(1,10) if i % 3 == 0))
print("Numbers not div 2 and 3: ", list(i for i in range(1,10) if i % 2 != 0 and i % 3 != 0))