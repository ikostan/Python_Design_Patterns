#!/usr/bin/env python3


class Transmission:

    def __init__(self, i):
        self._type = self.get_types().get(i, None)

    def get_types(self):
        return {1: 'Manual', 2: 'Automatic', 3: 'CVT', 4: 'Semi-automatic'}

    def get_transmission(self):
        return self._type
