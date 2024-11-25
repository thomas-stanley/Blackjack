import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return self.__str__()

def card_setup():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [Card(rank, suit) for rank in ranks for suit in suits] * 6  # 6 Deck shoe
    random.shuffle(deck)
    return deck

def main():
    cards = card_setup()
    print(cards)

if __name__ == "__main__":
    main()