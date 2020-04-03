import  user_chapter_8 as user

class Privileges:

    def __init__(self, privileges=['can add post', 'can delete post', 'can edit post']):
        self.privileges = privileges

    def showPrivileges(self):
        if isinstance(self.privileges, list):
            print(self.privileges)
            return self.privileges


class Admin(user.User):

    def __init__(self, firstName, lastName, age, loginAttempts):
        super().__init__(firstName, lastName, age, loginAttempts)
        self.privileges = Privileges()
