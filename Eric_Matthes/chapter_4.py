car = "BMW"
if car == "BMW":
    print("I love BMW!")
    print(car == "BMW")

car = "bmw"
if car != "BMW":
    print("I love another car")
    print(car == "BMW")

weapon = "rifle"
if weapon == "rifle":
    print(weapon == "rifle")

if weapon != "sword":
    print(weapon == "sword")

house = "mine"
if house == "mine":
    print("I love my house")
    print(house == "mine")

if house != "his":
    print("Actually it's his house")
    print(house == "his")

food = ['pizza', 'cacao', 'coffee']
if 'pizza' in food:
    print("I love pizza!")
    print('pizza' in food)
    print(food[0].title())

if 'vodka' not in food:
    print("I don't like vodka")
    print("vodka" not in food)

if 'water' not in food:
    print("We dont't have some water")
    print("water" in food)

if 'coffee' in food:
    print("We don't have some coffee!")
    print("coffee" not in food)
    print(food[2].title())

building = "grey"
if building == "grey":
    print("Is building grey? " + str(building == "grey"))

if building != 'red':
    print("Is building red? " + str(building == "red"))

myString = "my string"
myStringV2 = "My String"
hisString = "his string"
hisStringV2 = "His string"
if myString == "my string":
    print(myString == "my string")

if myString != myStringV2:
    print(myString == myStringV2)

if hisString == hisStringV2.lower():
    print(hisString == hisStringV2.lower())

if hisString != hisStringV2:
    print(hisString == hisStringV2)

number1 = 10
number2 = 15
number3 = 10
number4 = 17

if number2 > number1:
    print("15 is bigger than 10 " + str(number2 > number1))

if number1 < number2:
    print("Is number 1 bigger than number2? " + str(number1 > number2))

if number1 == number3:
    print("Does 10 equal to 10? " + str(number1 == number3))

if number4 != number2:
    print("Does number2 equal to number 4? " + str(number2 == number4))

if number4 >= number2:
    print("Does number4 equal or bigger than number2? " + str(number4 >= number2))

if number1 >= number3:
    print("Does number1 equal or bigger than number3? " + str(number1 >= number3))

if number4 <= number2:
    print("Does number2 equal or less than number4 " + str(number4 <= number2))

if number3 <= number4:
    print("Does number4 equal or less than number3 " + str(number4 <= number3))

if number4 >= number2 and number3 >= number1:
    print("It's true " + str(number4 >= number2) + " " + str(number3 >= number1))

if number1 <= number4 and number2 >= number3:
    print("One true and one false " + str(number1 >= number4) + " " + str(number2 >= number3))

print("It's false " + str(number1 >= number4 and number2 >= number3))

if number4 >= number2 or number3 >= number1:
    print(number4 >= number2 or number3 >= number1)

if number1 >= number1 or number2 >= number3:
    print("One true and one false, but we use 'OR' and we have true on the finish "
          + str(number1 >= number4 or number2 >= number3))

newList = ['1', '2']
if '1' in newList:
    print("We have 1 in our list")

if '3' not in newList:
    print("Unfortunately we don't have 3 in our list")

alien_color = 'green'
if alien_color == 'green':
    print("My congratulations! You have earned the 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("It's fail version of the program")

alien_color = 'yellow'
if alien_color == 'green':
    print("My congratulations! You have earned the 5 points!")

elif alien_color != 'green':
    print("My congratulations! You have earned the 10 points!")

else:
    print("We have a mistake!")

alien_color = 'green'
if alien_color == 'green':
    print("If block")

else:
    print("The color's mistake")

alien_color = 'yellow'
if alien_color == 'green':
    print("If block")

else:
    print("Else block")

alien_color = 'yellow'
if alien_color == 'green':
    print("My congratulations! You have earned the 5 points!")

elif alien_color == 'yellow':
    print("My congratulations! You have earned the 10 points!")

elif alien_color == 'red':
    print("My congratulations! You have earned the 15 points!")

else:
    print("The mistake!")

age = 65
if not isinstance(age, int):
    print("You can use only numbers")

elif age < 2 and age >= 0:
    print("The person is a baby")

elif age >= 2 and age < 4:
    print("The person is a toddler")

elif age >= 4 and age < 13:
    print("The person is a kid")

elif age >= 13 and age < 20:
    print("The person is a teenager")

elif age >= 20 and age < 65:
    print("The person is an adult")

elif age >= 65:
    print("The person is an elder")

elif age < 0:
    print("It's impossible")

else:
    print("We have the mistake of enter")

favoriteFruits = ['fruits', 'vegetables', 'pizza']
if 'fruits' in favoriteFruits:
    print("You really like eating fruits!")

if 'coffee' in favoriteFruits:
    print("You really like drinking coffee!")

if 'vegetables' in favoriteFruits:
    print("You really like eating vegetables!")

if 'meat' in favoriteFruits:
    print("You really like eating meat!")

if 'pizza' in favoriteFruits:
    print("You really like eating pizza")

if 'fish' in favoriteFruits:
    print("You really like eating fish!")

userNamesList = ['kostya', 'igor', 'andrew', 'andy', 'pike', 'admin']
userName = 'igor'
if not userNamesList:
    print("We need to find some users!")

elif userName == 'admin':
    print("Hello admin, do you need something?")

elif userName not in userNamesList:
    print("Sorry, but this name doesn't exist. We don't have " + userName + " in our database")

else:
    print("Hello " + userName)

currentUsers = ['KOstya', 'IGOR', 'andrew', 'andy', 'pike', 'admin']
newUsers = ['kostya', 'igor', 'admin', 'sonya', 'clarke']
currentUsersLower = []
for currentUser in currentUsers:
    currentUsersLower.append(currentUser.lower())

for newUser in newUsers:
    if not isinstance(newUser, str):
        print("You can use only string!")

    elif newUser.lower() in currentUsersLower:
        print("Sorry, but you will need to enter a new username. The username " + newUser + " is busy")

    else:
        print("The username " + newUser + " is available")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for number in numbers:
    if number == 1:
        print(str(number) + "st")

    if number == 2:
        print(str(number) + "nd")

    if number == 3:
        print(str(number) + "rd")

    if number == 0:
        print("zero")

    else:
        print(str(number) + "th")









