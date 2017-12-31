#!/usr/div/env python3
import time
from proxy_sample.producer import Producer


class Proxy:
    def __init__(self):
        self._occupied = False
        self._producer = None

    def set_occupied(self, param):
        self._occupied = param

    def produce(self):
        print("Artist checking if Producer is available...")
        if self._occupied is True:
            self._producer = Producer()
            time.sleep(2)
            self._producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy!")
