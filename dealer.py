import deck
import player
import setup
class Dealer:
    def __init__(self):
        self.hand = setup.Setup().deal_hand()
    
def main():
    test_dealer = Dealer()
    print(test_dealer.hand)


if __name__ == "__main__":
    main()