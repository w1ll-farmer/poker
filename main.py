import check_hands
import random

CARDS = [[i for i in range(1,15)] for j in range(4)]
SUITS = {1: "hearts", 2: "clubs", 3: "diamonds", 4: "spades"}

class Card:
    def __init__(self,rank, suit):
        self.rank =rank
        self.suit = suit
        

class Player:
    def __init__(self, name, blind, hand):
        self.name = name
        self.bank = (20+50+100+200+500)*1000
        self.blind = blind
        self.hand = hand
        
    def update_bank(self, difference):
        self.bank += difference
        
    def update_blind(self, blind):
        self.blind = blind
        
    def update_hand(self, hand):
        self.hand = hand
        
        
        
d = Card(4,"Hearts")       

     
     
def end_round(activePlayers,pot):
    scores = []
    for player in activePlayers:
        if check_hands.is_royal_flush(hand):
            scores.append(9)
        elif check_hands.is_straight_flush(player.hand):
            scores.append(8)
        elif check_hands.is_4_of_a_kind(player.hand):
            scores.append(7)
        elif check_hands.is_full_house(player.hand):
            scores.append(6)
        elif check_hands.is_flush(player.hand):
            scores.append(5)
        elif check_hands.is_straight(player.hand):
            scores.append(4)
        elif check_hands.is_3_of_a_kind(player.hand):
            scores.append(3)
        elif check_hands.is_2_pair(player.hand):
            scores.append(2)
        elif check_hands.is_pair(player.hand) > 0:
            scores.append(1)
        else:
            scores.append(max(player.hand)-14)
    highest = -12
    highestPlayers = []
    for i in range(0, len(activePlayers)):
        if scores[i] > highest:
            highest = scores[i]
            highestPlayers = [activePlayers[i]]
        elif scores[i] == highest:
            highestPlayers.append(activePlayers[i])
    
    for i in highestPlayers:
        i.update_bank(pot/len(highestPlayers))
        
        
    
    
    
    
    