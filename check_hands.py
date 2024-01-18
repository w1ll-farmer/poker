def is_flush(s1, s2, s3, s4, s5):
    if s1 == s2 == s3 == s4 == s5:
        return True
    
def is_straight(c1, c2, c3, c4, c5):
    count = 0
    hand = [c1, c2, c3, c4, c5]
    i=0
    if len(list(set(hand))) != len(hand):
        return False
    while count <= 1 and i <= 4:
        if hand[i]+1 not in hand and (hand[i]+1) % 13 not in hand:
            count+=1
        i+=1
    if 13 in hand and 2 in hand:
        return False
    if count > 1:
        return False
    else:
        return True

def is_straight_flush(s1, c1, s2, c2, s3, c3, s4, c4, s5, c5):
    if is_flush(s1, s2, s3, s4, s5) and is_straight(c1, c2, c3, c4, c5):
        return True
    else:
        return False

def is_pair(hand):
    # hand = [c1, c2, c3, c4, c5]
    for i in range(0, len(hand)):
        if len([x for x in hand if x == hand[i]]) == 2:
            return  hand[i]
    return -1

def is_2_pair(hand):
    pairCard = is_pair(hand)
    if pairCard != -1:
        shorthand = [card for card in hand if card != pairCard]
        if is_pair(shorthand) != -1:
            return True
    return False

def is_3_of_a_kind(hand):
    for i in range(0, len(hand)):
        if len([card for card in hand if card == hand[i]]) == 3:
            return True
    return False

def is_full_house(hand):
    if is_3_of_a_kind(hand) and is_pair(hand):
        return True
    return False

def is_4_of_a_kind(hand):
    for i in range(0, len(hand)):
        if len([card for card in hand if card == hand[i]]) == 4:
            return True
    return False

def is_royal_flush(s1, c1, s2, c2, s3, c3, s4, c4, s5, c5):
    if is_straight_flush(s1, c1, s2, c2, s3, c3, s4, c4, s5, c5):
        if len([rank for rank in [c1,c2,c3,c4,c5] if rank ==10]) > 0 and len([rank for rank in [c1,c2,c3,c4,c5] if rank ==14]) > 0:
            return True
    return False

print(is_royal_flush(1,10,1,11,1,12,1,13,1,14))
print(is_straight(13,14,2,3,4))

