# class Restaurant:
#
#     def __init__(self, name, cuisine, numberServed):
#         self.numberServed = 0
#         self.name = name
#         self.cuisine = cuisine
#
#     def describeRestaurant(self):
#         print(f"The restaurant {self.name.title()} welcomes you. Our cuisine: {self.cuisine.title()}")
#
#     def openRestaurant(self):
#         print(f"The restaurant {self.name.title()} is open!")
#
#     def makeDictionary(self):
#         restaurant = {self.cuisine: {}}
#         restaurant[self.cuisine]['name'] = self.name
#         print(restaurant)
#
#     def setNumberServed(self, number):
#         self.numberServed = number
#
#     def incrementNumberServed(self, number):
#         if number < 0:
#             number = number * (-1)
#
#         self.numberServed += number
#
#
# a = Restaurant('dragon', 'chinese', 52)
# print(f"{a.name.title()} and {a.cuisine.title}")
# a.describeRestaurant()
# a.openRestaurant()
# a.makeDictionary()
# b = Restaurant('puzata hata', 'ukrainian', 23)
# c = Restaurant('mushlya', 'seafood', 45)
# b.describeRestaurant()
# c.describeRestaurant()
# b.openRestaurant()
# c.openRestaurant()
# b.makeDictionary()
# c.makeDictionary()
# d = Restaurant('Tokugawa', 'japanese', 52)
# print(d.numberServed)
# d.numberServed = 52
# print(d.numberServed)
# d.setNumberServed(13)
# print(d.numberServed)
# d.incrementNumberServed(2)
# print(d.numberServed)
# d.incrementNumberServed(-2)
# print(d.numberServed)

class User:

    def __init__(self, firstName, lastName, age, loginAttempts):
        self.loginAttempts = 0
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def describeUser(self):
        print(f" Your first name is: {self.firstName.title()},\n Your last name is: {self.lastName.title()},\n Your "
              f"age is: {self.age}")

    def greetUser(self):
        fullName = self.firstName + " " + self.lastName
        print(f"Hello {fullName.title()}, I'm glad to see you again!")

    def incrementLoginAttemps(self):
        self.loginAttempts += 1

    def resetLoginAttempts(self):
        self.loginAttempts = 0


a = User("constantine", "yachnytskyi", "27", 2)
b = User("ingrid", "korsgard", "28", 3)
c = User("kate", "sporysh", "29", 4)
a.describeUser()
a.greetUser()
b.describeUser()
b.greetUser()
c.describeUser()
c.greetUser()
print(a.loginAttempts)
a.incrementLoginAttemps()
print(a.loginAttempts)
a.incrementLoginAttemps()
a.incrementLoginAttemps()
print(a.loginAttempts)
a.resetLoginAttempts()
print(a.loginAttempts)