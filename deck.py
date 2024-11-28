import cards
class Deck:
    def __init__(self):
        self.shuffle()
    
    def deal(self):
        return self.deck.pop()
    
    def shuffle(self):
        self.deck = cards.card_setup()


def main():
    test_deck = Deck()
    print(test_deck.deal())
    test_deck.shuffle()
    print(test_deck.deal())


if __name__ == "__main__":
    main()