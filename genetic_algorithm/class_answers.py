# -*- coding: sjis -*-
import sys, os

# �ϐ��ɂ��Ă��܂��Ɠǂݎ���p�ɂł��Ȃ�
# ���̂��߁A�N���X�Ƃ��Ē�`����
class class_answers:

    __answers = []      # ��

    @property
    def answers(self):
        return self.__answers

    def __init__(self):
        self.__answers = [3, 1, 2, 2, 2, 3, 1, 3, 3, 1]
            
