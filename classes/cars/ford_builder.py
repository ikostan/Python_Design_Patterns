#!/usr/bin/env python3
from builder_sample.builder.builder import Builder


class Ford(Builder):
    """
        Concrete Builder class
            --> provides car_parts and tools in order to create an specific type of a ca
    """

    def add_model(self):
        self.car._model = "Ford"

    def add_tires(self):
        self.car._tires = "Regular tires"

    def add_engine(self):
        self.car._engine = "v6"

    def add_gear(self):
        self.car._gear = "Automate"

