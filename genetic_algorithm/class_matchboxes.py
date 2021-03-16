# -*- coding: sjis -*-
import sys, os
import random

import class_matchbox

# 1個体用のクラス
class class_matchboxes:

    MAX_NUM = 10        # 保有するマッチ箱の数

    __no = 0            # 順位
    __matchboxes = []   # 保有するマッチ箱のリスト
    __score = 0         # 総得点

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
        # クラス変数として解釈されてしまうのを防ぐため
        self.__matchboxes = []
        self.__score = 0

        # マッチ箱を生成する
        for i in range(self.MAX_NUM):
            self.__matchboxes.append(class_matchbox.class_matchbox())

    # 交叉
    def closs(self, dice_num, src_group):
        # 2～10を対象とするそれ以外は何もしない
        if dice_num < 2 or self.MAX_NUM < dice_num:
            return

        if dice_num == 2:
            self.__matchboxes[0] = src_group[0]
        else:
            self.__matchboxes[0:dice_num-2] = src_group[0:dice_num-2]

    # 突然変異
    def mutant(self, dice_num):
        # 2～11を対象とするそれ以外は何もしない
        if dice_num < 2 or self.MAX_NUM+1 < dice_num:
            return

        # 2～10は対応する箱をそのまま対象とする
        # 11は1問目の箱を対象とする
        num = 0 if dice_num == self.MAX_NUM+1 else dice_num - 1

        # 1つずつずらすと2つずらさなければ正解にならない場合に終わらなくなる
        # そのため、ランダム値で突然変異させる様に変更した
        '''
        if self.__matchboxes[num].stick_num == 3:
            self.__matchboxes[num].stick_num = 1
        else:
            self.__matchboxes[num].stick_num += 1
        '''
        self.__matchboxes[num].stick_num = random.randint(1, 3)

    # 1個体の得点を算出する
    def calc_score(self):
        self.__score = 0
        for matchbox in self.__matchboxes:
            self.__score += matchbox.score
            
    # 解答を確認する
    def open_matchboxes(self, ans):
        if ans is None:
            return

        for i, matchbox in enumerate(self.__matchboxes):
            matchbox.score = 10 if matchbox.stick_num == ans.answers[i] else 0

