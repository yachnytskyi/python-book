person = {
    'name': 'ingrid',
    'lastname': 'korsgard',
    'age': '28',
    'city': 'chicago'
}

print("Her name is: " + person['name'].title())
print("Her lastname is: " + person['lastname'].title())
print("Her age is: " + person['age'])
print("Her city is: " + person['city'].title())

favoriteNumbers = {
    'ingrid': '7',
    'kostya': '13',
    'igor': '0',
    'denis': '666',
    'natalie': '777'
}

print("\nIngrid's favorite number is: " + favoriteNumbers['ingrid'])
print("Kostya's favorite number is: " + favoriteNumbers['kostya'])
print("Igor's's favorite number is: " + favoriteNumbers['igor'])
print("Denis's's favorite number is: " + favoriteNumbers['denis'])
print("Natalie's favorite number is: " + favoriteNumbers['natalie'])

glossary = {
    'dictionary': "It's a special data storage for any objects. We can add lists, ints, strings and other data "
                  "structures, "
                  "even other dictionaries",
    'if-elif-else': "We use these structures for adding additional options in our programs",
    'tuple': "They are very similar on lists, just they are immutable, we can't change data in their",
    'list': 'We can put our data in lists, and then extract data from list on index (list[0])',
    'int': "It's a special data type for numbers"
}

print('dictionary: ' + glossary['dictionary'])
print('if-elif-else: ' + glossary['if-elif-else'])
print('tuple: ' + glossary['tuple'])
print('list: ' + glossary['list'])
print(('int: ' + glossary['int']))

print('\nThe new glossary')
glossary['testItem'] = 'something'
glossary['newItem'] = 'something new'
glossary['thirdItem'] = 'third'
glossary['fourthItem'] = '4th'
glossary['fifthItem'] = '5th'
for key, value in glossary.items():
    print(key + ": " + value)

rivers = {
    'nile': 'egypt',
    'mississippi': 'the USA',
    'dnipro': 'ukraine'
}

print("\n")
for key, value in rivers.items():
    print(key.title() + " runs through" + value.title())

print("\n")
for key in rivers.keys():
    print("I guess that " + key.title() + " is amazing river")

for value in rivers.values():
    print("I guess that " + value.title() + " is amazing country")

print("\n")
favoriteLanguages = {
    'ingrid': 'python',
    'kate': 'python',
    'kostya': 'ruby',
    'andrew': 'kotlin',
    'pavlo': 'java',
    'martin': 'c#',
}

people = ['kostya', 'igor', 'martin', 'natalie', 'denis']

for key, value in favoriteLanguages.items():
    if key in people:
        print("Hey " + key.title() + ", thank you for your responding!")

    elif key not in people:
        print("Hey " + key.title() + ", I suppose you to take the poll!")

    else:
        print("Unknown mistake")

person1 = {
    'name': 'kate',
    'lastname': 'sporysh',
    'age': '29',
    'city': 'kyiv'
}

person2 = {
    'name': 'natalie',
    'lastname': 'zinchenko',
    'age': '25',
    'city': 'nijin'
}

person3 = {
    'name': 'kostya',
    'lastname': 'yachnytskyi',
    'age': '27',
    'city': 'lviv'
}

print('\n')

peopleList = [person1, person2, person3]
for person in peopleList:
    print(person)

pet1 = {
    'kind': 'wolf',
    'owner': 'costya',
}

pet2 = {
    'kind': 'cat',
    'owner': 'natalie'
}

pet3 = {
    'kind': 'dog',
    'ownder': 'denis'
}

print("\n")
pets = [pet1, pet2, pet3]

for pet in pets:
    print(pet)

favoritePlaces = {
    'kostya': ['forests', 'grand canyon', 'seas'],
    'igor': ['spain', 'moscow', 'startup', 'django'],
    'denis': ['abhazia', 'russia', 'belarus'],
}

for key, value in favoritePlaces.items():
    print("Hey " + key.title() + ", your favorite places are:")
    for place in value:
        print("\t" + place.title())

newDictionary = {
    'ukraine': ['kyiv'],
    'russia': ['moscow'],
    'the usa': ['washington'],
    'japan': ['tokyo'],
    'china': ['pekin'],
}

print("\n")

for key, value in newDictionary.items():
    print("The capital of " + key.title() + " is:")
    for capital in value:
        print("\t" + capital.title())

happyNumbers = {
    'ingrid': ['1', '2'],
    'kostya': ['3', '4', '5'],
    'igor': ['6', '7', '8', '9'],
    'denis': [10, 11, 12, 13, 14],
    'natalie': [15, 16, 17, 18, 19, 20]
}

print("\n")
for key, value in happyNumbers.items():
    print("Hey " + key + ", your favorite numbers are:")
    for number in value:
        print("\t" + str(number))

cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': '3 millions',
        'fact': 'khreshatyk street'
    },

    'moscow': {
        'country': 'russia',
        'population': '30 millions',
        'fact': 'red square'
    },

    'london': {
        'country': "the uk",
        'population': '20 millions',
        'fact': 'trafalgar square'
    },
}

for key, value in cities.items():
    print("The facts about " + key.title() + " are:")
    for a, b in value.items():
        print("\t" + a.title() + ": " + b.title())

print("\n Another way for inputting them")
for key, value in cities.items():
    print("The facts about " + key.title() + " are:")
    country = value['country']
    population = value['population']
    fact = value['fact']

    print("\tCountry: " + country.title())
    print("\tPopulation: " + population.title())
    print("\tFact: " + fact.title())

developers = {
    'constantine': {
        'level': 'junior',
        'languages': ['c#', 'java', 'ruby', 'python'],
        'style': 'remote'
    },
    'igor': {
        'level': 'architector',
        'languages': ['c#', 'python', 'go', 'rust'],
        'style': 'office/remote',
    }
}

print("\nThe last dictionary")
for key, value in developers.items():
    print("Description of " + key.title() + ":")
    level = value['level']
    languages = value['languages']
    style = value['style']
    print("\t" + level.title())
    print("\t" + str(languages))
    print("\t" + style)

print("\nThe last task")
target = 'go'
for key, value in developers.items():
    if target in value['languages']:
        print(key.title() + " - you are really now " + "'" + target.title() + "'" + "! That's wonderful!")
        print("Your level is: " + value['level'] +
              ", your languages are: " + str(value['languages']) + " and your style is: " + value['style'])
