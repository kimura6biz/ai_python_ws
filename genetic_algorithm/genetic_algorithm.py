# -*- coding: sjis -*-
import sys, os
import class_matchboxes
import copy
import operator

import class_answers
import class_dice

MATCHBOX_GROUP_NUM = 10
PERFECT_SCORE = 100

# �������킹�����ē��_���Z�o����
def answer(groups, ans):
    # �̐����J��Ԃ�
    for i, group in enumerate(groups):
        # �𓚂��m�F�������ł����10�_���l������
        group.open_matchboxes(ans)

        # ���v���_���Z�o����
        # 100�_���l���������_�ŏI������
        group.calc_score()

        # =========================================
        # �r���o�߂����邽�߂̃R���\�[���o��
        # =========================================
        print("==============�}�b�`���̒��g==============")
        print("[���_]:", group.score, " [�{��]:", end="")
        for matchbox in group.matchboxes:
            print(matchbox.stick_num, end="")
        print("")
        print("==========================================")
        
        if group.score == PERFECT_SCORE:
            return i+1

    return 0

# ���_�Ń\�[�g���ď��ʂ��ӂ�Ȃ���
def rank(groups):
    groups = sorted(groups, reverse=True, key=operator.attrgetter('score'))

    for i, group in enumerate(groups):
        group.no = i+1

    return groups

# �T�C�R����2��U���č��v��Ԃ�
def roll_dice():
    dice_num = 0
    dice = class_dice.class_dice()
    for i in range(2):
        dice_num += dice.num

    return dice_num

# ���2�̂�e�Ƃ��ĉ���2�̂𐶐�����
def reborn(groups):
    # ����2�𓑑�����
    for i in range(2):
        del groups[-1]

    # ���2��e�Ƃ��q�𐶐�����
    groups.append(copy.deepcopy(groups[0]))
    groups.append(copy.deepcopy(groups[1]))

    return groups

# ����2�̂���������
def closs(groups):
    # 2�̃T�C�R����U���������
    dice_num = roll_dice()
    temp = copy.deepcopy(groups[8])
    groups[8].closs(dice_num, groups[9].matchboxes)
    groups[9].closs(dice_num, temp.matchboxes)

    return groups

# ����2�̂ɓˑR�ψق��N����
def mutant(groups):
    # 2�̃T�C�R����U��ˑR�ψق���
    dice_num = roll_dice()
    groups[8].mutant(dice_num)

    # 2�̃T�C�R����U��ˑR�ψق���
    dice_num = roll_dice()
    groups[9].mutant(dice_num)

    return groups

# ��`�q���󂯌p��
def inherit(groups):
    groups = reborn(groups)
    groups = closs(groups)
    groups = mutant(groups)

    return groups

def main(argv):
    # �}�b�`����10�̗p�ӂ���
    groups = []
    for i in range(MATCHBOX_GROUP_NUM):
        groups.append(class_matchboxes.class_matchboxes())

    ans = class_answers.class_answers()     # ��

    i = 0
    while True:
        # =========================================
        # �r���o�߂����邽�߂̃R���\�[���o��
        # =========================================
        print("=================================================================================")
        print("                                     {0}��ځ@�@�@�@�@�@�@�@�@�@�@�@�@�@         ".format(i+1))
        print("=================================================================================")

        print("==================������==================")
        for a in ans.answers:
            print(a, end="")
        print("")
        print("==========================================")

        if answer(groups, ans) > 0:
            print("[", i+1, "]��ڂŏI��")
            break

        # ���_���ɏ��ʂ�t����
        groups = rank(groups)
        groups = inherit(groups)

        i+=1

    input()
    return 0

if os.path.splitext(os.path.basename(sys.argv[0]))[0] == os.path.splitext(os.path.basename(__file__))[0]: sys.exit(main(sys.argv))
