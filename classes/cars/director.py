#!/usr/bin/env python3


class Director:
    """Director class"""
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        # From abstract Builder class
        self._builder.create_car()
        # From Concrete Builder class
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.get_car()
