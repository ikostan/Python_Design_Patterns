#!/usr/bin/env python3
from classes.cars.car import Car


class Builder:
    """Abstract Builder class"""
    def __init__(self):
        self.car = None

    def create_car(self):
        self.car = Car()

    def get_car(self):
        return self.car
