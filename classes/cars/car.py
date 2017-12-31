#!/usr/bin/env python3


class Car:
    """Car product"""
    def __init__(self):
        self._model = None
        self._tires = None
        self._engine = None
        self._gear = None

    def __str__(self):
        return '{}, {}, {}, {}'.format(self._model, self._tires, self._engine, self._gear)
