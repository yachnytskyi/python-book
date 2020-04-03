filename = 'first_text_file.txt'

with open(filename) as fileObject:
    contents = fileObject.read()
    print(contents.rstrip())
    print(contents.rstrip())
    print(contents.rstrip())

with open(filename) as fileObject:
    for line in fileObject in range(0, 3):
        print(line.rstrip())
        print(line.rstrip())
        print(line.rstrip())