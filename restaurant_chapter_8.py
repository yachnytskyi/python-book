class Restaurant:

    def __init__(self, name, cuisine, numberServed):
        self.numberServed = 0
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

    def setNumberServed(self, number):
        self.numberServed = number

    def incrementNumberServed(self, number):
        if number < 0:
            number = number * (-1)

        self.numberServed += number
