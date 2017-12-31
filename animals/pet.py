#!/usr/bin/env python3
from animals.animal import Animal


class Pet(Animal):
    """ A simple Pet class """
    def __init__(self, word, name):
        Animal.__init__(self, word)
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
