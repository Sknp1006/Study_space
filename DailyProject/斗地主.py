import random as R

cards = []
def creat_cards():
    kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
    # 黑桃('\u2660')
    # 梅花('\u2663')
    # 红桃('\u2665')
    # 方块('\u2666')
    num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    joker = ['大王', '小王']
    for x in kinds:
        for y in num:
            cards.append(x+y)
    cards.extend(joker)
    return cards

def hand_cards():
    R.shuffle(creat_cards())
    # print(len(cards))
    player_1 = cards[0:17]
    player_2 = cards[17:34]
    player_3 = cards[34:51]
    buttom = cards[51:54]
    input()
    print("第一个人的手牌:", player_1)
    input()
    print("第一个人的手牌:", player_2)
    input()
    print("第一个人的手牌:", player_3)
    input()
    print("底牌:", buttom)

hand_cards()