# -*- coding: sjis -*-
import sys, os

# 変数にしてしまうと読み取り専用にできない
# そのため、クラスとして定義する
class class_answers:

    __answers = []      # 解答

    @property
    def answers(self):
        return self.__answers

    def __init__(self):
        self.__answers = [3, 1, 2, 2, 2, 3, 1, 3, 3, 1]
            
