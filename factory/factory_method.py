#!/usr/bin/env python3
from animals.dog import Dog
from animals.cat import Cat
from animals.pet import Pet
from animals.animal import Animal


def get_pet(pet):
    """The factory method"""
    pets = dict(dog=Dog('Max'), cat=Cat('Tom'))
    return pets[pet]


def get_type(pet):
    print('Class: {}'.format(type(pet)))
    print('Is Animal: {}'.format(isinstance(pet, Animal)))
    print('Is Pet: {}'.format(isinstance(pet, Pet)))
    print('Name: {}'.format(pet.get_name()))
    print('Speak: {}'.format(pet.speak()))
    print()


def main():
    print('Factory pattern:\n')
    pet = get_pet('dog')
    get_type(pet)

    pet = get_pet('cat')
    get_type(pet)


if __name__ == '__main__':
    main()
