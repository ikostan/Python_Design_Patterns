#!/usr/bin/env python3


class Adapter:
    def __init__(self, obj, **adapted_method):
        self._object = obj
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)
