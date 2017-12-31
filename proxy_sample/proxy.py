#!/usr/div/env python3
import time


class Proxy:

    def __init__(self):
        self._ocupied = False
        self._producer = None

    def produce(self):
        print("Artist checking if Producer is available...")

        if self._ocupied is False:
            pass
        else:
            time.sleep(2)
            print("Producer is busy!")
