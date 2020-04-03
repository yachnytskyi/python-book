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


