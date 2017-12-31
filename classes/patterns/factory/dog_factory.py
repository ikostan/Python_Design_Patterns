#!/usr/bin/env python3
from classes.animals.dog import Dog


class DogFactory:
    """Concrete Factory"""

    def get_pet(self, name):
        return Dog(name)

    def get_food(self):
        return "Dog Food"
