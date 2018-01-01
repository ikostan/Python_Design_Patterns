#!/usr/bin/env python3
from adapter_sample.korean import Korean
from adapter_sample.british import British
from adapter_sample.adapter import Adapter


"""
Adapter converts the interface of a class into another one a client is expecting.
This time our problem is that the interfaces are incompatible between a client and a server.
In our scenario, we have Korean and British objects which have different method names for speaking.
Instead, the client would like to use a uniform interface that is the speak method.
Our solution is the use of the adapter pattern that translates the method names
in between the client and the server code.

Bridges and decorators are related to the adapter pattern.
"""


def main():

    print('Adapter example:\n')

    objects = []
    korean = Korean()
    british = British()
    objects.append(Adapter(korean, speak=korean.speak_korean()))
    objects.append(Adapter(british, speak=british.speak_english()))


    for i in objects:
        print('{} says: {}'.format(i._name, i.speak))


if __name__ == '__main__':
    main()
