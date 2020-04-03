filename = 'first_text_file.txt'

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
