#!/usr/bin/env python3

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


if __name__ == '__main__':
    main()
