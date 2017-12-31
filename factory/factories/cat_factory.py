#!/usr/bin/env python3
from animals.cat import Cat


class CatFactory:
    """Concrete Factory"""

    def get_pet(self, name):
        return Cat(name)

    def get_food(self):
        return "Cat Food"
