# -*- coding: sjis -*-
import sys, os
import random

class class_matchbox:

    __stick_num = 0 # マッチ棒の数
    __score = 0     # 得点

    @property
    def stick_num(self):
        return self.__stick_num

    @stick_num.setter
    def stick_num(self, stick_num):
        self.__stick_num = stick_num

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def __init__(self):
        self.__stick_num = random.randint(1, 3)

