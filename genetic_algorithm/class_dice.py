# -*- coding: sjis -*-
import sys, os
import random

# �T�C�R����͋[
class class_dice:

    __num = 0

    @property
    def num(self):
        return random.randint(1, 6)

    def __init__(self):
        self.__num = 0
        return
