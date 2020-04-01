# Task 1
# developers = {
#     'constantine': {
#         'level': 'junior',
#         'languages': ['c#', 'java', 'ruby', 'python'],
#         'style': 'remote'
#     },
#     'igor': {
#         'level': 'architector',
#         'languages': ['c#', 'python', 'go', 'rust'],
#         'style': 'office/remote',
#     }
# }
#
# active = True
#
# while active:
#     name = input("Please enter the names (constantine/igor)")
#
#     if name in developers:
#         section = input("Please enter the sections (level/languages/style")
#         print(type(developers[name][section]))
#
#         if section in developers[name]:
#             if isinstance(developers[name][section], list):
#                 for language in developers[name][section]:
#                     print(language)
#             else:
#                 print(developers[name][section])
#
#         else:
#             print("Please enter the correct section")
#
#     else:
#         print("Please fill the correct name")
#
#     if name == 'q':
#         active = False


#Task 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(c)

class Finder:

    def __init__(self, listA, listB):
        self.listA = listA
        self.listB = listB

    def dublicatesFinder(self):
        listC = []
        if isinstance(self.listA, list) and isinstance(self.listB, list):
            for i in self.listA:
                for j in self.listB:
                    if i == j and i not in listC:
                        listC.append(i)
            print(listC)

        else:
            print("You can use only lists as the parameters!")

        return listC


a = Finder([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
a.dublicatesFinder()
print(a.listA)
print(a.listB)

b = Finder("Fake", "fake2")
b.dublicatesFinder()
print(b.listA)
print(b.listB)


class MaximumKeys:

    def __init__(self, keysDictionary):
        self.keysDictionary = keysDictionary

    def finderKeys(self):
        firstValue = 0
        secondValue = 0
        thirdValue = 0
        firstKey = ''
        secondKey = ''
        thirdKey = ''

        if isinstance(self.keysDictionary, dict):
            for key, value in self.keysDictionary.items():
                if value > firstValue:
                    thirdValue = secondValue
                    secondValue = firstValue
                    firstValue = value
                    thirdKey = secondKey
                    secondKey = firstKey
                    firstKey = key

                elif value > secondValue and value < firstValue:
                    thirdValue = secondValue
                    secondValue = value
                    thirdKey = secondKey
                    secondKey = key

                elif value > thirdValue and value < secondValue:
                    thirdValue = value
                    thirdKey = key

            print(f"The first key is: {firstKey}, his value is: {firstValue}")
            print(f"The third key is: {secondKey}, his value is: {secondValue}")
            print(f"The third key is: {thirdKey}, his value is: {thirdValue}")

        else:
            print("Sorry, but you can use only dictionary as a parameter")

        return firstValue, secondValue, thirdValue, firstKey, secondKey, thirdKey


a = MaximumKeys({'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20})
a.finderKeys()

print("\n")
b = MaximumKeys({'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'j': 52852, 'z': 5215125})
b.finderKeys()
c = MaximumKeys(['a'])
c.finderKeys()


class Second:

    def __init__(self, seconds):
        self.seconds = seconds

    def finderSeconds(self):
        nativeSeconds = self.seconds
        secondsAmount = 0
        minutesAmount = 0
        hoursAmount = 0
        daysAmount = 0
        active = True

        while active:
            if isinstance(self.seconds, int) and self.seconds > 0:

                if self.seconds - 24 * 60 * 60 >= 0:
                    daysAmount += 1
                    self.seconds -= 24 * 60 * 60
                    continue

                elif self.seconds - 60 * 60 >= 0:
                    hoursAmount += 1
                    self.seconds -= 60 * 60
                    continue

                elif self.seconds - 60 >= 0:
                    minutesAmount += 1
                    self.seconds -= 60
                    continue

                elif self.seconds - 60 <= 0:
                    secondsAmount += self.seconds
                    active = False

                else:
                    active = False

                print(f"Hello. We have {daysAmount} days, {hoursAmount} hours, "
                      f"{minutesAmount} minutes and {secondsAmount} seconds in {nativeSeconds}")

            else:
                print(f"Sorry, but you can use only positive numbers ( which > 0 ). {self.seconds} its' not the positive "
                      f"number")
                active = False


a = Second(24 * 60 * 60 + 3601)
a.finderSeconds()
fake = Second(-1)
fake.finderSeconds()
fakeType = Second('5')
fake.finderSeconds()

class StringBuilder:

    def __init__(self, string):
        self.string = string

    def stringSum(self):
        if isinstance(self.string, str):
            result = int(self.string) + int(self.string * 2) + int(self.string * 3)
            print(result)

        elif isinstance(self.string, int):
            intString = str(self.string)
            result = int(intString) + int(intString * 2) + int(intString * 3)
            print(result)

        else:
            print(f"Sorry, but you can use only string or int type for the parameter! {self.string} "
                  f"its'not a string/int type!")


a = StringBuilder("5")
a.stringSum()
b = StringBuilder("2")
b.stringSum()
c = StringBuilder("3")
c.stringSum()
intType = StringBuilder(5)
intType.stringSum()
fakeType = StringBuilder(['a'])
fakeType.stringSum()