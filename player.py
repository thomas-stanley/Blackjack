import deck
class Player:
    def __init__(self):
        self.hand = []
    
    def hand(self):
        self.hand.append(deck.Deck().deal())
        self.hand.append(deck.Deck().deal())
