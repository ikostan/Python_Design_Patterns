#!/usr/bin/env python3
from classes.cars.ford_builder import Ford
from classes.cars.bmw_builder import BMW
from classes.cars.director import Director


def main():
    """
        Builder is a solution to an Anti-Pattern called Telescoping Constructor.
        An Anti-Pattern is the opposite of the best practice.
        The Telescoping Constructor Anti-Pattern occurs when a software developer
        attempts to build a complex object using an excessive number of constructors.
        The Builder pattern is trying to solve this problem.
        Think of a scenario, in which you're trying to build a car.
        This requires various car car_parts to be first constructed individually and then assembled.

        The Builder pattern brings an order to this chaotic process to remove this unnecessary
        complexity in building a complex object.
        The Builder partitions the process of building a complex object into the four different roles.
        The first role is Director, and Director is in charge of actually building
        a product using the builder object.
        Then, the builder class provides all the necessary interfaces
        required in building an object. We call this an Abstract Builder,
        because there will be a Concrete Builder inheriting from this Abstract Builder.

        The Concrete Builder class inherits from the Builder class and
        actually implements the details of the interfaces of the Builder class,
        for a specific type of a product. And the product represents an object being built.
        The Builder Pattern does not rely on polymorphism, unlike Factory and Abstract Factory.
        The focus of the Builder Pattern is rather on reducing the complexity of
        building a complex object through a divide and conquer strategy.
    """
    print('Builder example:\n')

    bmw = BMW(8, 1)  # Concrete Builder
    director = Director(bmw)  # Director instance using instance of a concrete class/builder
    director.construct_car()
    car1 = director.get_car()
    print(car1)

    ford = Ford(6, 2)  # Concrete Builder
    director = Director(ford)  # Director instance using instance of a concrete class/builder
    director.construct_car()
    car2 = director.get_car()
    print(car2)


if __name__ == '__main__':
    main()
