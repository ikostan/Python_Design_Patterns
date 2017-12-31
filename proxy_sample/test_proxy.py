#!/usr/div/env python3
"""
Proxy becomes handy when creating an object that is very resource intensive.
The problem we need to solve here is to postpone our object creation as long as possible,
due to the resource intensive nature of the object we're creating.
Therefore, there is a need for a placeholder which will in turn create
the object if its creation is absolutely necessary. So here is our scenario.
So in our scenario, we create this instance of the Producer class only when he's available,
because only a fixed number of Producer objects can exist at a given time.

Our Proxy in this case is an artist who is checking to see if the Producer becomes available for a guest.
In the Proxy design pattern clients interact with a Proxy object most of the time until
the resource intensive object becomes available.
Therefore, the Proxy object is in charge of creating the resource intensive objects.
Adapter and Decorator are related to the Proxy design pattern.
"""


def main():
    print("Proxy test:\n")


if __name__ == "__main__":
    main()