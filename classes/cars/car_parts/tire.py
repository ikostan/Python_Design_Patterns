#!/usr/bin/env python3


class Tire:

    def __init__(self, i):
        self._tire = self.get_types().get(i, None)

    def get_types(self):
        return {1: 'Sport', 2: 'Regular', 3: 'Winter'}

    def get_tire(self):
        return self._tire