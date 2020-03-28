car = input("Hey friend, which car would you like to get?")
print("So let me see if I can find you a " + car.title())

cars = ['subaru', 'bmw', 'mercedes', 'lexus']
if car in cars:
    print(f'Great! You can get a {car.title()} for yourself!')

elif car not in cars:
    print(f"Unfortunately, we don't have a {car.title()}. But we can suppose all of our cars: {cars}")

else:
    print(f"Unknown error")

print("\n the dictionary garage")
garage = {
    'our': {
        'name': 'Our garage',
        'cars': ['subaru', 'bmw', 'mercedes', 'lexus', 'toyota'],
    },
    'kyiv': {
        'name': "Kyiv's garage",
        'cars': ['mazda', 'nissan', 'ferrari']
    }
}

for key, value in garage.items():
    if car in value['cars']:
        print(f"Great! You can get a {car.title()} for yourself in {key.title()}'s garage")

    elif car not in value['cars']:
        print(f"Unfortunately, we don't have a {car.title()} in {key.title()}'s garage. But we can suppose all of our "
              f"cars: {value['cars']}")

restaurant = {
    'group1': {
        'name': 'wolfs',
        'amount': '8',
    },
    'group2': {
        'name': 'dogs',
        'amount': '5'
    },
    'group3': {
        'name': 'people',
        'amount': '25',
    },
}

amount = input("How many people are in your group?")
amount = int(amount)
if int(amount) < 0:
    amount = int(amount) * (-1)

for key, value in restaurant.items():
    temp = int(value['amount']) + int(amount)
    if temp > 8:
        print(f"You'll need to wait for a {value['name']}'s table")

    elif temp > 0 and temp <= 8:
        print(f"You can get {value['name']}'s table")

    else:
        print("Unknown error")

number = input("Please enter your number")
if int(number) % 10 == 0:
    print(f"Your number {int(number)} is multiple of 10")

else:
    print(f"Your number {int(number)} isn't multiple of 10")

active = True
pizza = []
ingredientList = ['tomato', 'pasta', 'cheese', 'cacao']
pizzaSecond = {
    'toppings': {
        'ingredients': []
    }
}

while active:
    topping = input("Please enter a topping for the pizza")
    if topping == 'exit':
        active = False

    elif topping not in ingredientList:
        print(f"Please enter any topping from out list {ingredientList}. Unfortunately,"
              f" we dont have a {topping} on our store")
        continue

    else:
        pizza.append(topping)
        for key, value in pizzaSecond.items():
            value['ingredients'] = pizza
            print(f"Our dictionary contains the following ingredients: \n{value['ingredients']}")

        print(f"You have added {topping} for the pizza!")
        print(f"The pizza contains the following components: \n{pizza}")

tickets = {
    'prices': {
        'baby': 'free',
        'toddler': '$10',
        'teenager': '$15',
    }
}

active = True
while active:
    age = input("Please enter your age")
    if age == 'exit':
        active = False

    elif age == 'quit':
        break

    elif int(age) >= 0 and int(age) < 3:
        print(f"The ticket costs {tickets['prices']['baby']}, because you are a baby")
        for key, value in tickets['prices'].items():
            if key == 'baby':
                print(f"The ticket costs {tickets['prices']['baby']}, because you are a {key}")

    elif int(age) >= 3 and int(age) <= 12:
        print(f"The ticket costs {tickets['prices']['toddler']}, because you are a toddler")
        for key, value in tickets['prices'].items():
            if key == 'toddler':
                print(f"The ticket costs {tickets['prices']['toddler']}, because you are a {key}")

    elif int(age) > 12:
        print(f"The ticket costs {tickets['prices']['teenager']}, because you are a teenager")
        for key, value in tickets['prices'].items():
            if key == 'teenager':
                print(f"The ticket costs {tickets['prices']['teenager']}, because you are a {key}")



# infinite loop
# a = 5
# while a == 5:
#     print(a)
