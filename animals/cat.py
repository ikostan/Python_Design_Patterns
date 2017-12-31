#!/usr/bin/env python3
from animals.pet import Pet


class Cat(Pet):
    """A simple Cat class"""
    def __init__(self, name):
        Pet.__init__(self, 'meow', name)

    def __str__(self):
        return "Cat"
