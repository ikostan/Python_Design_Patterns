#!/usr/bin/env python3


class PetStore:
    """PetStore houses Abstract Factory"""

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self, name):
        """Utility method to display the details of the objects returned by the DogFactory"""
        pet = self._pet_factory.get_pet(name)
        pet_food = self._pet_factory.get_food()
        print('Our pet is a {}. He says {} and he eats {}.'.format(pet, pet.speak(), pet_food))
