import restaurant_chapter_8 as restaurant
import user_chapter_8 as user
import admin_chapter_8 as admin
from collections import OrderedDict
from random import randint



class IceCreamStand(restaurant.Restaurant):

    def __init__(self, name, cuisine, numberServed, flavors):
        super().__init__(name, cuisine, numberServed)
        self.flavors = flavors

    def showFlawords(self):
        if isinstance(self.flavors, list):
            print(self.flavors)
        else:
            print("You can use only list")


g = IceCreamStand('dragon', 'chinese', 152, ['rose', 'mushrooms', 'flowers'])
g.showFlawords()
a = restaurant.Restaurant('dragon', 'chinese', 52)
print(f"{a.name.title()} and {a.cuisine.title}")
a.describeRestaurant()
a.openRestaurant()
a.makeDictionary()
b = restaurant.Restaurant('puzata hata', 'ukrainian', 23)
c = restaurant.Restaurant('mushlya', 'seafood', 45)
b.describeRestaurant()
c.describeRestaurant()
b.openRestaurant()
c.openRestaurant()
b.makeDictionary()
c.makeDictionary()
d = restaurant.Restaurant('Tokugawa', 'japanese', 52)
print(d.numberServed)
d.numberServed = 52
print(d.numberServed)
d.setNumberServed(13)
print(d.numberServed)
d.incrementNumberServed(2)
print(d.numberServed)
d.incrementNumberServed(-2)
print(d.numberServed)


a = admin.Admin("kostya", 'yachnytskyi', 27, 1)
a.describeUser()
a.greetUser()
a.privileges.showPrivileges()
a = user.User("constantine", "yachnytskyi", "27", 2)
b = user.User("ingrid", "korsgard", "28", 3)
c = user.User("kate", "sporysh", "29", 4)
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

class Battery:
    def __init__(self, batterySize):
        self.batterySize = batterySize

    def checkBatterySize(self):
        if self.batterySize != 85:
            self.batterySize = 85
            return  self.batterySize

a = OrderedDict()
a['a'] = 5
a['b'] = 6
a['c'] = 7
a['d'] = 9

print(a)


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def rollDie(self):
        for x in range(0, 10):
            x = randint(1, self.sides)
            print(x)

        return x


a = Die()
a.rollDie()
b = Die(20)
b.rollDie()


