import json

#filename = 'first_text_file.txt'

# with open(filename) as fileObject:
#     contents = fileObject.read()
#     print(contents.rstrip() * 3)
#
# with open(filename) as fileObject:
#     for line in fileObject:
#         print(line.rstrip())
#
# with open(filename) as fileObject:
#     lines = fileObject.readlines()
#
# for line in lines:
#     print(line.rstrip())
#
# with open(filename) as fileObject:
#     lines = fileObject.readlines()
#
# ourString = ''
# for line in lines:
#     ourString += line
#
# print(ourString)
# print(len(ourString))

# with open(filename) as fileObject:
#     lines = fileObject.readlines()
#
# oldString = ''
# newString = ''
# for line in lines:
#     oldString += line
#
# newString = oldString.replace('Python', 'Ruby')
# print(f"Our old string is:\n{oldString}")
# print(f"Our new string is:\n{newString}")

# filename = "guest.txt"
# name = input("Please enter your name")
# with open(filename, 'w') as fileObject:
#     fileObject.write(name)

# filename = "guest_book.txt"
# active = True
#
# while active:
#     name = input("Please enter your name")
#     if name == 'q':
#         active = False
#     else:
#         print(f"Hello {name}!")
#         with open(filename, 'a') as fileObject:
#             fileObject.write(f"It's name {name}\n")

# filename = "poll_book.txt"
# active = True
# reasons = {}
# while active:
#     name = input("Please enter your name")
#     reason = input("Why do you like programming?")
#     additional = input("Do you have additional reasons? (yes/no)")
#     reasons = {name: {}}
#     if name != 'q' or reason != 'q' or additional != 'q':
#         reasons[name][reason] = reason
#     if name == 'q' or reason == 'q' or additional == 'q':
#         active = False
#     elif additional == 'yes':
#         while active:
#             reason = input("Why do you like programming?")
#             additional = input("Do you have additional reasons? (yes/no)")
#             if additional == 'no' or reason == 'q' or reason == 'no':
#                 reasons[name][reason] = reason
#                 print(reasons)
#                 with open(filename, 'a') as fileObject:
#                     fileObject.write(f"{name} likes programming because: {reasons}\n")
#                 active = False
#             elif additional == 'yes':
#                 reasons[name][reason] = reason
#                 print(reasons)
#                 with open(filename, 'a') as fileObject:
#                     fileObject.write(f"{name} likes programming because: {reasons}\n")
#     elif additional == 'no':
#         reasons[name][reason] = reason
#         print(reasons)
#         with open(filename, 'a') as fileObject:
#             fileObject.write(f"{name} likes programming because: {reasons}\n")

# while active:
#     name = input("Please enter your name")
#     reason = input("Why do you like programming?")
#     additional = input("Do you have additional reasons? (yes/no)")
#     reasons = []
#     if name != 'q' or reason != 'q' or additional != 'q':
#         reasons.append(reason)
#     if name == 'q' or reason == 'q' or additional == 'q':
#         active = False
#     elif additional == 'yes':
#         while active:
#             reason = input("Why do you like programming?")
#             additional = input("Do you have additional reasons? (yes/no)")
#             if additional == 'no' or reason == 'q' or reason == 'no':
#                 reasons.append(reason)
#                 print(reasons)
#                 with open(filename, 'a') as fileObject:
#                     fileObject.write(f"{name} likes programming because: {reasons}\n")
#                 active = False
#             elif additional == 'yes':
#                 reasons.append(reason)
#                 print(reasons)
#     elif additional == 'no':
#         reasons.append(reason)
#         print(reasons)
#         with open(filename, 'a') as fileObject:
#             fileObject.write(f"{name} likes programming because: {reasons}\n")


# while True:
#     firstNumber = input("Enter the first number")
#     if firstNumber == 'q':
#         break
#     secondNumber = input("Enter the second number")
#     if secondNumber == 'q':
#         break
#     try:
#         result = int(firstNumber) * int(secondNumber)
#     except ValueError:
#         print("Please enter only numbers!")
#     else:
#         print(result)

# filename = "cats.txt"
# catString = ''
# try:
#     with open(filename) as fileObject:
#         lines = fileObject.readlines()
# except FileNotFoundError:
#     # print(f"Sorry, but file {filename} does not exist")
#     pass
# else:
#     for line in lines:
#         catString += line
#
# print(catString)
# print(len(catString))
#
# filename = "dogs.txt"
# dogString = ''
# try:
#     with open(filename) as fileObject:
#         lines = fileObject.readlines()
# except FileNotFoundError:
#     print(f"Sorry, but file {filename} does not exist")
# else:
#     for line in lines:
#         dogString += line
#
# print(dogString)
# print(len(dogString))

# filename = 'gutenberg.txt'
# textString = ""
# try:
#     with open(filename) as fileObject:
#         lines = fileObject.readlines()
# except FileNotFoundError:
#     pass
# else:
#     for line in lines:
#         textString += line
#
# theCount = textString.count("the")
# theLowerCount = textString.lower().count("the")
# print(f"We have {theCount} times the word 'the' in our text")
# print(f"We have {theLowerCount} times the word 'the'(with underline) in our text")


# filename = "favorite_number.json"
#
# try:
#     with open(filename) as fileObject:
#         favoriteNumber = json.load(fileObject)
# except FileNotFoundError:
#     number = input("Enter your number")
#     with open(filename, 'w') as fileObject:
#         json.dump(number, fileObject)
#         print(f"We have written your favorite number {number}!")
# else:
#     print(f"Your favorite number is: {favoriteNumber}")

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    correctUsername = input(f"Is {username} your correct username? (yes/no)")
    if correctUsername == 'yes':
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()




