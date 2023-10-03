# persons.py
class Persons:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"
