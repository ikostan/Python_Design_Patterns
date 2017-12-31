#!/usr/bin/env python3
from factory.factories.dog_factory import DogFactory
from factory.factories.cat_factory import CatFactory
from factory.factories.pet_store import PetStore


def main():
    print('Factory pattern:\n')

    dog_factory = DogFactory()
    shop = PetStore(dog_factory)
    shop.show_pet('Bob')

    cat_factory = CatFactory()
    shop = PetStore(cat_factory)
    shop.show_pet('Tob')


if __name__ == '__main__':
    main()
