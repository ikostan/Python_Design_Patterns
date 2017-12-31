#!/usr/bin/env python3


class Animal:
    """ A simple Animal class """
    def __init__(self, word):
        self._word = word

    def speak(self):
        return self._word

