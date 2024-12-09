import setup
class Dealer:
    def __init__(self):
        self.hand = setup.Setup().deal_hand()
        self.total = self.hand[0].value
    
    
def main():
    test_dealer = Dealer()
    print(test_dealer.hand)


if __name__ == "__main__":
    main()