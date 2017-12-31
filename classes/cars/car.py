#!/usr/bin/env python3


class Car:
    """Car product"""
    def __init__(self):
        self._model = None
        self._tires = None
        self._engine = None
        self._transmission = None

    def set_model(self, model):
        self._model = model

    def set_tires(self, tires):
        self._tires = tires

    def set_engine(self, engine):
        self._engine = engine

    def set_transmission(self, transmission):
        self._transmission = transmission

    def __str__(self):
        return '{}, {}, v{}, {}'.format(self._model, self._tires, self._engine, self._transmission)
