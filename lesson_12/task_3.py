list1 = ['1', '2', '3', '4', '5', '7']

list2 = list(map(int, list1))

list3 = []
for item in list1:
    list3.append(int(item))
 
print (list3)

print("Map func: ", list2)
print("Append func: ", list3)