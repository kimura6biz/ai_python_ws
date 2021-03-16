# -*- coding: sjis -*-
import sys, os
import random

import class_matchbox

# 1�̗p�̃N���X
class class_matchboxes:

    MAX_NUM = 10        # �ۗL����}�b�`���̐�

    __no = 0            # ����
    __matchboxes = []   # �ۗL����}�b�`���̃��X�g
    __score = 0         # �����_

    @property
    def no(self):
        return self.__no

    @no.setter
    def no(self, no):
        self.__no = no

    @property
    def matchboxes(self):
        return self.__matchboxes

    @property
    def score(self):
        return self.__score

    def __init__(self):
        # �N���X�ϐ��Ƃ��ĉ��߂���Ă��܂��̂�h������
        self.__matchboxes = []
        self.__score = 0

        # �}�b�`���𐶐�����
        for i in range(self.MAX_NUM):
            self.__matchboxes.append(class_matchbox.class_matchbox())

    # ����
    def closs(self, dice_num, src_group):
        # 2�`10��ΏۂƂ��邻��ȊO�͉������Ȃ�
        if dice_num < 2 or self.MAX_NUM < dice_num:
            return

        if dice_num == 2:
            self.__matchboxes[0] = src_group[0]
        else:
            self.__matchboxes[0:dice_num-2] = src_group[0:dice_num-2]

    # �ˑR�ψ�
    def mutant(self, dice_num):
        # 2�`11��ΏۂƂ��邻��ȊO�͉������Ȃ�
        if dice_num < 2 or self.MAX_NUM+1 < dice_num:
            return

        # 2�`10�͑Ή����锠�����̂܂ܑΏۂƂ���
        # 11��1��ڂ̔���ΏۂƂ���
        num = 0 if dice_num == self.MAX_NUM+1 else dice_num - 1

        # 1�����炷��2���炳�Ȃ���ΐ����ɂȂ�Ȃ��ꍇ�ɏI���Ȃ��Ȃ�
        # ���̂��߁A�����_���l�œˑR�ψق�����l�ɕύX����
        '''
        if self.__matchboxes[num].stick_num == 3:
            self.__matchboxes[num].stick_num = 1
        else:
            self.__matchboxes[num].stick_num += 1
        '''
        self.__matchboxes[num].stick_num = random.randint(1, 3)

    # 1�̂̓��_���Z�o����
    def calc_score(self):
        self.__score = 0
        for matchbox in self.__matchboxes:
            self.__score += matchbox.score
            
    # �𓚂��m�F����
    def open_matchboxes(self, ans):
        if ans is None:
            return

        for i, matchbox in enumerate(self.__matchboxes):
            matchbox.score = 10 if matchbox.stick_num == ans.answers[i] else 0

