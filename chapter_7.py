from modul_chapter_6 import buildCars
from modul_chapter_6 import buildProfile as createProfile
import modul_chapter_6
import modul_chapter_6 as mc_6
from modul_chapter_6 import *

def display_message():
    print("Hey! It's my first function today!")


display_message()


def favoriteBook(book):
    print(f"My favorite book is {book.title()}")


favoriteBook("witcher")


def makeShirt(size='large', message='I love python'):
    print(f"Your t-shirt's size: {size} and message: {message}")


makeShirt('small', 'hello')
makeShirt(message='hello world', size='medium')
makeShirt()
makeShirt(message="Something wrong")
makeShirt(size='small')


def describeCity(city, country='Ukraine'):
    print(f"{city} is in {country}")


describeCity('Kyiv')
describeCity('Kyiv', 'Ukraine')
describeCity('Lviv', 'Poland')
describeCity('Prague')


def cityAndCountry(city, country):
    homeTown = ['lviv', 'kyiv', 'chernihiv']
    countryList = ['ukraine', 'poland', 'slovakia']
    if city in homeTown:
        print(f"Hey, we are from one city! I am also from {city}")

    if country in countryList:
        print(f"Hey, we are from one country! I am also from {country}")

    result = city + ' ' + country
    return result


active = True

while active:
    city = input("Please, enter your city")
    country = input("Please, enter your country")
    if city == 'q' or country == 'q':
        active = False

    result = cityAndCountry(city, country)
    print(result)


def makeAlbum(name, album, tracks=""):
    storage = {'name': name, 'album': album}

    if tracks != "":
        storage['tracks'] = tracks

    return storage


print(makeAlbum('beatles', 'album', '52'))
print(makeAlbum('second', 'sth', 23))
print(makeAlbum('third', 'sth'))

active = True

while active:
    name = input("Enter your name")
    album = input("Enter your album")
    tracks = input("Enter amount of your tracks (it's optional)")

    if name == 'q' or album == 'q' or tracks == 'q':
        active = False

    result = makeAlbum(name, album, tracks)
    print(result)


def showMagicians(magicians):
    greateMagicians = []
    for magician in magicians:
        magician = magician + " Great"
        print(f"Hey {magician.title()}!")
        greateMagicians.append(magician)

    return greateMagicians


storage = ['kostya', 'ingrid', 'kate']
print(showMagicians(storage))
print(storage)

def makeSandwiches(*sandwiches):
    print("Making a pizza with the following ingredients:")
    for sandwich in sandwiches:
        print(sandwich)

makeSandwiches("tomato", "banana")
makeSandwiches("grocery")

def buildProfile(firstName, lastName, **userProfile):
    profile = {'firstName': firstName, 'lastName': lastName}
    for key, value in userProfile.items():
        profile[key] = value
    return profile

igorProfile = createProfile(firstName='igor', lastName='kramer', position='architector', city='moscow')
constantineProfile = createProfile(firstName='constantine', lastName='yachnytskyi', work='remote', country='ukraine')
print(igorProfile)
print(constantineProfile)
fakeProfile = createProfile(firstName='fake', lastName='fake')
print(fakeProfile)

def buildCars(country, manufacture, model, **car):
    cars = {country: {}}
    cars[country]['manufacture'] = manufacture
    cars[country]['model'] = model
    for key, value in car.items():
       cars[country][key] = value
    return cars


bmw = buildCars('germany', "bmw", "X5", color='black', weight='2 tones')
fake = buildCars('fake', "fake", "fake", weight=100000)
mercedes = buildCars('germany', "mercedes", "sth", color='white', weight='3 tones', value='$100000')
print(bmw)
print(fake)
print(mercedes)
