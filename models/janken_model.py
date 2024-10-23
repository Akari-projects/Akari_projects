import random

def judge(player_hand, akari_hand):
    if player_hand == akari_hand:
        return "引き分け"
    elif (player_hand == "グー" and akari_hand == "チョキ") or \
         (player_hand == "チョキ" and akari_hand == "パー") or \
         (player_hand == "パー" and akari_hand == "グー"):
        return "勝ち"
    else:
        return "負け"

def get_random_hand():
    return random.choice(["グー", "チョキ", "パー"])
