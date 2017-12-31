#!/usr/bin/env python3
import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_obj(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_obj(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
