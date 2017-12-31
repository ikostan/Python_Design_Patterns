#!/usr/bin/env python3
from classes.patterns.factory.dog_factory import DogFactory
from classes.patterns.factory.cat_factory import CatFactory
from classes.patterns.factory.pet_store import PetStore


def main():
    """
    Factory encapsulates object creation.
    That is, Factory is an object specializing in creating other objects.

    The Factory pattern is useful, especially when you're not sure about
    what type of objects you'll be needing eventually in your system.

    Another possibility is the situation in which your application needs
    to decide on what class to use at run time. Here is a scenario we'll be using in our coding exercise.

    Your pet shop was only selling dogs but now you need to sell cats, too.
    Therefore, your system needs to be able to handle cats as well as dogs.
    Your system's supposed to show how each of the pets you sell speak.
    """

    print('Factory pattern:\n')
    print('Define an interface for creating an object, '
          'but let subclasses decide which class to instantiate. '
          '\nFactory Method lets a class defer instantiation to subclasses.\n')

    dog_factory = DogFactory()
    shop = PetStore(dog_factory)
    shop.show_pet('Bob')

    cat_factory = CatFactory()
    shop = PetStore(cat_factory)
    shop.show_pet('Tob')


if __name__ == '__main__':
    main()
