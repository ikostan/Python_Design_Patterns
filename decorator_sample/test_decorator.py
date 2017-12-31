#!/usr/div/env python3
from functools import wraps

"""
    Python makes implementing Decorator very straightforward due to its built in language features. 
    Our challenge here is to add additional features to an existing object dynamically without using subclassing. 
    Here's our scenario. We start with a function simply displaying a Hello World! message, 
    and then we'd like to make the message look fancier by decorating it with additional tags, 
    such as blink, as you can see here.
    Functions are also objects in Python, and we can simply add additional features to these 
    functions using this built in decorator feature in Python. 
    Patterns such as adapter, composite, and strategy are related to the decorator pattern.
"""

def make_blink(function):
    """Defines the decorator"""
    @wraps(function)  # makes the decorator transparent in terms of its name and docstring
    def decorator():
        # Add a new functionality to the decorated function
        ret = function()
        return "<blink>" + ret + "</blink>"
    return decorator


@make_blink
def hello_world():
    return "Hello World!"


def main():
    print("Decorator test:\n")

    print(hello_world())

    print(hello_world.__name__)
    print(hello_world.__doc__)


if __name__ == "__main__":
    main()