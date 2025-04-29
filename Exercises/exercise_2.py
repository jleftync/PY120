"""
Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.
The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.
The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.
Yes, this class is somewhat contrived.
You can use the following code snippets to test your class. Since some tests cause exceptions, we've broken them into separate snippets.
"""

class Person:
    
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)
    
    @property
    def name(self):
        first_name = self._first_name
        last_name = self._last_name
        return first_name + " " + last_name
    
    @name.setter
    def name(self, full_name):
        first_name, last_name = full_name
        self._set_name(first_name, last_name)
        
    
    @classmethod
    def verify(cls, name):
        if name.isalpha() == False:
            raise ValueError("Name must be alphabetical")
    
    def _set_name(self, first_name, last_name):
        Person.verify(first_name)
        Person.verify(last_name)
        self._first_name = first_name
        self._last_name = last_name
    