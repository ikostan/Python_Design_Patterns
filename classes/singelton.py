#!/usr/bin/env python3
from classes.borg import Borg


class Singelton():

    def __init__(self, **kwargs):
        """Updates an attributes dictionary by inserting a new key-value pairs"""
        Borg.__init__(self)

    def __str__(self):
        """Returns the attribute dictionary for printing"""
