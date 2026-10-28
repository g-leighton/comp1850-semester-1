# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        '''
        Creates a person with fields for their name and date of birth.
        '''

        if not isinstance(name, (str)):
            raise TypeError("Name must be a string.")
        
        if name == "":
            raise ValueError("Name cannot be empty.")
        
        if not isinstance(birth, (date)):
            raise TypeError("Date must be a date object.")
        
        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        '''
        Finds the persons initials from their inputted name.
        '''

        initials_list = ""
        for i in range(0, len(self.name)):
            if self.name[i].isupper():
                initials_list += self.name[i]
        
        return initials_list

    def is_birthday(self):
        '''
        Checks if today is the persons birthday.
        '''

        if date.today() == self.birth:
            return "True"
        else:
            return "False"

""" test = Person("George Leighton", date.today())

print(test.initials())
print(test.is_birthday()) """