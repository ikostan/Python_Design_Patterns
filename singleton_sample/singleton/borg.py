#!/usr/bin/env python3


class Borg:
    """Borg class holds global attributes"""
    _shared_state = {}

    def __init__(self):
        """Create an attributes dictionary"""
        self.__dict__ = self._shared_state
