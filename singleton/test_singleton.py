#!/usr/bin/env python3


def main():
    """
        An object-oriented way of providing global variables is Singleton.
        Singleton is the pattern you need when you'd like to allow only one object
        to be instantiated from a class.

        Creating a global variable in an object-oriented way is Singleton.
        Why would you need such a pattern?
        Let's say that there is a need for keeping a cache of information
        to be shared by various elements of your software system.
        By keeping this information in the single object,
        there's no need to retrieve the information from its original source every time.

        So in this case, Singleton acts as a cache of the information.
        Modules in Python act as Singletons.
        There are also a number of ways of implementing Singleton,
        but we'll be using the Borg design pattern to implement our Singleton.
    """
    print('Singleton example:\n')


if __name__ == '__main__':
    main()
