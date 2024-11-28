import cards
class Deck:
    def __init__(self):
        self.deck = cards.Card().card_setup()
    
    def deal(self):
        return self.deck.pop()