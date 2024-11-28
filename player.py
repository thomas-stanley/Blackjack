import deck
class Player:
    def __init__(self):
        self.hand = []
    
    def deal_hand(self):
        self.hand.append(deck.Deck().deal())
        self.hand.append(deck.Deck().deal())
        return self.hand


def main():
    test_player = Player()
    print(test_player.deal_hand())
    print(test_player.hand)


if __name__ == "__main__":
    main()