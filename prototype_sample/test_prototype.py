#!/usr/bin/env python3
from classes.cars.car import Car
from prototype_sample.prototype import Prototype


def main():
    """
        The prototype class has four different methods, and we'll start with the init method.
        In the init method, all we're doing is simply creating this dictionary object.
        The dictionary object will be containing the objects that will be cloned.
        So let's create the dictionary object by typing self._objects,
        and then the second method is register object.
    """

    print('Prototype pattern:\n')

    car = Car()
    car.set_engine(4)
    car.set_model("Honda")
    car.set_transmission("Automatic")
    car.set_tires("Regular")

    prototype = Prototype()
    prototype.register_obj("Honda", car)
    clone = prototype.clone("Honda")
    print(clone)


if __name__ == '__main__':
    main()
