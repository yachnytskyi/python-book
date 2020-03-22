dishes = ['texas', 'margarita', 'pepperoni']
for dish in dishes:
    print(dish)
    print("I like " + dish + " pizza so much!")

print("For example, \nTexas pizza,\nMargarita pizza and\n Pepperoni pizza.\nI really love pizza!")

for value in range(1, 20):
    print(value)

#for value in range(1, 1000000):
 #   print(value)

million = []
for value in range(1, 1000000):
    million.append(value)

print(max(million), '\n',  min(million), '\n', sum(million))

for value in range(1, 20, 2):
    print(value)

trees = [value for value in range(3, 30, 3)]
print(trees)

trees = []
for value in range(3, 30, 3):
    trees.append(value)

print(trees)

cube = [value**3 for value in range(1, 10)]
print(cube)

cube = []
for value in range(1, 10):
    cube.append(value**3)

print(cube)


