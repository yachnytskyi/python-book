developers = {
    'constantine': {
        'level': 'junior',
        'languages': ['c#', 'java', 'ruby', 'python'],
        'style': 'remote'
    },
    'igor': {
        'level': 'architector',
        'languages': ['c#', 'python', 'go', 'rust'],
        'style': 'office/remote',
    }
}

active = True

while active:
    name = input("Please enter the names (constantine/igor)")

    if name in developers:
        section = input("Please enter the sections (level/languages/style")
        print(type(developers[name][section]))

        if section in developers[name]:
            if isinstance(developers[name][section], list):
                for language in developers[name][section]:
                    print(language)
            else:
                print(developers[name][section])

        else:
            print("Please enter the correct section")

    else:
        print("Please fill the correct name")

    if name == 'q':
        active = False
