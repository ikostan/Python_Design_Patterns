#!/usr/bin/env python3
from animals.pet import Pet


class Dog(Pet):
    """A simple Dog class"""
    def __init__(self, name):
        Pet.__init__(self, 'woof', name)

    def __str__(self):
        return "Dog"
