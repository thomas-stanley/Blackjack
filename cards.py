import random
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self) -> str:
        return self.__str__()

def card_setup(num_decks: int = 6) -> list:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [Card(rank, suit) for rank in ranks for suit in suits] * num_decks
    random.shuffle(deck)
    return deck

def main():
    cards = card_setup()
    print(cards)

if __name__ == "__main__":
    main()