import random
class Card:
    def __init__(self, rank: str, suit: str, value: int):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self) -> str:
        return self.__str__()

def card_setup(num_decks: int = 6) -> list:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }
    deck = [Card(rank, suit, values[rank]) for rank in ranks for suit in suits] * num_decks
    random.shuffle(deck)
    return deck

def main():
    cards = card_setup()
    print(cards)
    print(len(cards))

if __name__ == "__main__":
    main()