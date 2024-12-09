import deck
class Setup:
    def __init__(self):
        self.deck = deck.Deck()
        self.hand = []
    
    def deal_hand(self) -> list:
        self.hand = [self.deck.deal() for i in range(2)]
        return self.hand
    


def main():
    test_setup = Setup()
    print(test_setup.deal_hand())


if __name__ == "__main__":
    main() 