# -*- coding: sjis -*-
import sys, os
import class_matchboxes
import copy
import operator

import class_answers
import class_dice

MATCHBOX_GROUP_NUM = 10
PERFECT_SCORE = 100

# 答え合わせをして得点を算出する
def answer(groups, ans):
    # 個体数分繰り返す
    for i, group in enumerate(groups):
        # 解答を確認し正解であれば10点を獲得する
        group.open_matchboxes(ans)

        # 合計得点を算出する
        # 100点が獲得した時点で終了する
        group.calc_score()

        # =========================================
        # 途中経過を見るためのコンソール出力
        # =========================================
        print("==============マッチ箱の中身==============")
        print("[得点]:", group.score, " [本数]:", end="")
        for matchbox in group.matchboxes:
            print(matchbox.stick_num, end="")
        print("")
        print("==========================================")
        
        if group.score == PERFECT_SCORE:
            return i+1

    return 0

# 得点でソートして順位をふりなおす
def rank(groups):
    groups = sorted(groups, reverse=True, key=operator.attrgetter('score'))

    for i, group in enumerate(groups):
        group.no = i+1

    return groups

# サイコロを2回振って合計を返す
def roll_dice():
    dice_num = 0
    dice = class_dice.class_dice()
    for i in range(2):
        dice_num += dice.num

    return dice_num

# 上位2個体を親として下位2個体を生成する
def reborn(groups):
    # 下位2個を淘汰する
    for i in range(2):
        del groups[-1]

    # 上位2個を親とし子を生成する
    groups.append(copy.deepcopy(groups[0]))
    groups.append(copy.deepcopy(groups[1]))

    return groups

# 下位2個体を交叉する
def closs(groups):
    # 2つのサイコロを振り交叉する
    dice_num = roll_dice()
    temp = copy.deepcopy(groups[8])
    groups[8].closs(dice_num, groups[9].matchboxes)
    groups[9].closs(dice_num, temp.matchboxes)

    return groups

# 下位2個体に突然変異を起こす
def mutant(groups):
    # 2つのサイコロを振り突然変異する
    dice_num = roll_dice()
    groups[8].mutant(dice_num)

    # 2つのサイコロを振り突然変異する
    dice_num = roll_dice()
    groups[9].mutant(dice_num)

    return groups

# 遺伝子を受け継ぐ
def inherit(groups):
    groups = reborn(groups)
    groups = closs(groups)
    groups = mutant(groups)

    return groups

def main(argv):
    # マッチ箱を10個体用意する
    groups = []
    for i in range(MATCHBOX_GROUP_NUM):
        groups.append(class_matchboxes.class_matchboxes())

    ans = class_answers.class_answers()     # 解答

    i = 0
    while True:
        # =========================================
        # 途中経過を見るためのコンソール出力
        # =========================================
        print("=================================================================================")
        print("                                     {0}回目　　　　　　　　　　　　　　         ".format(i+1))
        print("=================================================================================")

        print("==================こたえ==================")
        for a in ans.answers:
            print(a, end="")
        print("")
        print("==========================================")

        if answer(groups, ans) > 0:
            print("[", i+1, "]回目で終了")
            break

        # 得点順に順位を付ける
        groups = rank(groups)
        groups = inherit(groups)

        i+=1

    input()
    return 0

if os.path.splitext(os.path.basename(sys.argv[0]))[0] == os.path.splitext(os.path.basename(__file__))[0]: sys.exit(main(sys.argv))
