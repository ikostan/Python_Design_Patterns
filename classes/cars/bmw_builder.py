#!/usr/bin/env python3
from builder_sample.builder.builder import Builder
from classes.cars.car_parts.transmission import Transmission
from classes.cars.car_parts.engine import Engine
from classes.cars.car_parts.tire import Tire


class BMW(Builder):
    """
        Concrete Builder class
            --> provides car_parts and tools in order to create an specific type of a ca
    """

    def add_model(self):
        self.car._model = "BMW"

    def add_tires(self):
        self.car._tires = Tire().get_tire()

    def add_engine(self):
        self.car._engine = Engine().get_engine()

    def add_transmission(self):
        self.car._transmission = Transmission(1).get_transmission()

