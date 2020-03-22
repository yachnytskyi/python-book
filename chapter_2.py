friends = ['denis', 'andrew', 'igor']
print(friends[0], friends[1], friends[2])
print("Hey " + friends[0].title() + ". What's up?")
print("Hey " + friends[1].title() + ". What's up?")
print("Hey " + friends[2].title() + ". What's up?")

wishes = ['laptop', 'tablet', 'pc']
print('I would like to have a ' + wishes[0].title() + ". That's amazing stuff!")
print('I would like to have a ' + wishes[1].title() + ". That's amazing stuff!")
print('I would like to have a ' + wishes[2].upper() + ". That's amazing stuff!")

guests = ['Tanya', 'Kate', 'Ingrid']
print('So, ladies ' + str(guests) + ' , I invite all of you on my dinner!')
print(guests[0] + ', I invite you on my dinner!')
print(guests[1] + ', I invite you on my dinner!')
print(guests[2] + ', I invite you on my dinner!')

del guests[0]
print("Unfortunately, Tanya won't able to come")
kate = guests.pop(0)
print("Unfortunately, " + kate + " won't able to come")
ingrid = "Ingrid"
guests.remove(ingrid)
print("Unfortunately, " + ingrid + " won't able to come")

guests.append('Kostya')
guests.append('Denis')
guests.append('Igor')
guests[0] = 'Alicia'
guests[1] = 'Natalie'
guests[2] = 'Lana'
print(guests[0] + ', I invite you on my dinner!')
print(guests[1] + ', I invite you on my dinner!')
print(guests[2] + ', I invite you on my dinner!')

guests.append('Bohdana')
guests.insert(2, 'Tanya')
guests.insert(5, 'Alex')
print(guests)
print(guests[0] + ', I invite you on my dinner!')
print(guests[1] + ', I invite you on my dinner!')
print(guests[2] + ', I invite you on my dinner!')
print(guests[3] + ', I invite you on my dinner!')
print(guests[4] + ', I invite you on my dinner!')
print(guests[5] + ', I invite you on my dinner!')

print("Sorry ladies, unfortunately I can invite only two people")
alicia = guests.pop(0)
print("Sorry " + alicia + " I just can invite only two people")
natalie = guests.pop(0)
print("Sorry " + natalie + " I just can invite only two people")
tanya = guests.pop(0)
print("Sorry " + tanya + " I just can invite only two people")
lana = guests.pop(0)
print("Sorry " + lana + " I just can invite only two people")
print("Hey " + guests[0] + ", you are still invited!")
print("Hey " + guests[1] + ", you are still invited!")
del guests[0]
del guests[0]
print(guests)

places = ['Grand Canyon', 'Yellowstone', 'Stonehenge', 'Texas', 'Okinawa']
print("Original order: " + str(places))
print("Temporally order: " + str(sorted(places)))
print("Original order: " + str(places))
places.reverse()
print("Reverse order: " + str(places))
places.reverse()
print("Original order: " + str(places))
places.sort()
print("Permanent order " + str(places))
places.sort(reverse=True)
print("Reverse order " + str(places))

guests.append('Guest')
print("I have invited " + str(len(guests)) + " on the dinner!")

countries = ['Ukraine', 'Japan', 'The US', 'The UK']
print(len(countries))
print(sorted(countries))
countries.reverse()
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
countries.append("Australia")
countries.insert(5, 'China')
print(countries)
countries[4] = 'India'
print(countries)
del countries[2]
print(countries)
india = countries.pop(3)
print(countries)
print("We have deleted " + india + " permanently")
countries.remove('The US')
print(countries)

# countries[5] it's a special mistake (the last exercise in the chapter 2)
