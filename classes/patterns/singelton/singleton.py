#!/usr/bin/env python3
from classes.patterns.singelton.borg import Borg


class Singleton(Borg):

    def __init__(self, **kwargs):
        """Updates an attributes dictionary by inserting a new key-value pairs"""
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        """Returns the attribute dictionary for printing"""
        return str(self._shared_state)
