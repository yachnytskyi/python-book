dishes = ['texas', 'margarita', 'pepperoni']
for dish in dishes:
    print(dish)
    print("I like " + dish + " pizza so much!")

print("For example, \nTexas pizza,\nMargarita pizza and\n Pepperoni pizza.\nI really love pizza!")

for value in range(1, 20):
    print(value)

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

mySlices = ['1', '2', '3', '4', '5', '6', '7', '8']
print("\n\nThe first three items in the list are: " + str(mySlices[:3]))
print("Three items from the middle of list are: " + str(mySlices[3:6]))
print("The last three last items in the list are: " + str(mySlices[-3:]))
print("The last three last items in the list are: " + str(mySlices[:-4:-1]))
print("All reserved items in the list are: " + str(mySlices[::-1]))


friend_dishes = dishes[:]
dishes.append('Alabama')
friend_dishes.append('California')
print("My favorite pizza are " + str(dishes))
print("My friend's favorite pizza are " + str(friend_dishes))
for dish in dishes:
    print(dish)

for friend_dish in friend_dishes:
    print(friend_dish)

for dish in dishes[:4]:
    dish = str(dish + "1")
    print(dish)

for friend_dish in friend_dishes[:2]:
    friend_dish = str(friend_dish + "5")
    print(friend_dish)

print("Original food:")
foods = ('coffee', 'cacao', 'cola', 'cheese', 'mushrooms')
for food in foods:
    print(food)

print("\nModified food:")
foods = ('coffee', 'vodka', 'porridge', 'cheese', 'mushrooms')
for food in foods:
    print(food)



