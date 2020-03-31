class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describeRestaurant(self):
        print(f"The restaurant {self.name.title()} welcomes you. Our cuisine: {self.cuisine.title()}")

    def openRestaurant(self):
        print(f"The restaurant {self.name.title()} is open!")

    def makeDictionary(self):
        restaurant = {self.cuisine: {}}
        restaurant[self.cuisine]['name'] = self.name
        print(restaurant)


a = Restaurant('dragon', 'chinese')
print(f"{a.name.title()} and {a.cuisine.title}")
a.describeRestaurant()
a.openRestaurant()
a.makeDictionary()
b = Restaurant('puzata hata', 'ukrainian')
c = Restaurant('mushlya', 'seafood')
b.describeRestaurant()
c.describeRestaurant()
b.openRestaurant()
c.openRestaurant()
b.makeDictionary()
c.makeDictionary()


class User:

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def describeUser(self):
        print(f" Your first name is: {self.firstName.title()},\n Your last name is: {self.lastName.title()},\n Your "
              f"age is: {self.age}")

    def greetUser(self):
        fullName = self.firstName + " " + self.lastName
        print(f"Hello {fullName.title()}, I'm glad to see you again!")


a = User("constantine", "yachnytskyi", "27")
b = User("ingrid", "korsgard", "28")
c = User("kate", "sporysh", "29")
a.describeUser()
a.greetUser()
b.describeUser()
b.greetUser()
c.describeUser()
c.greetUser()