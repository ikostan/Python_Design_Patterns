#!/usr/bin/env python3


class Engine:

    def __init__(self, cylinders):
        if 0 < cylinders < 13:
            self._cylinders = cylinders
        else:
            raise Exception("Cylinders number must be between 0 and 12")

    def get_engine(self):
        engine = 'v{}'.format(self._cylinders)
        return engine
