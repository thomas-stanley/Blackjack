import deck
class Setup:
    def __init__(self):
        self.hand = []
    
    def deal_hand(self):
        self.hand.append(deck.Deck().deal())
        self.hand.append(deck.Deck().deal())
        return self.hand


def main():
    test_setup = Setup()
    print(test_setup.deal_hand())
    print(test_setup.hand)


if __name__ == "__main__":
    main() 