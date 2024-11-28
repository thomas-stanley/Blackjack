import setup
import dealer
class Player:
    def __init__(self):
        self.hand = setup.Setup().deal_hand()
        self.dealer_hand = dealer.Dealer().hand
        self.user_options = {
            "hit": self.hit,
            "stand": self.stand,
            "double": self.double,
            "surrender": self.surrender
        } 
        if self.hand[0].rank == self.hand[1].rank:
            self.user_options["split"] = self.split
        if self.dealer_hand[0].rank == "A":
            self.user_options["insurance"] = self.insurance

    def action(self) -> str:
        valid_choice = False
        print("Choose an action: ")
        for option in self.user_options:
            print(option)
        user_choice = input().lower()
        while not valid_choice:
            if user_choice in self.user_options:
                valid_choice = True
                self.user_options[user_choice]()
            else:
                print("Invalid choice. Please try again.")
    
    def hit(self):
        self.hand.append(setup.Setup().deck.deal())

    def stand(self):
        print("Stand executed")
    
    def double(self):
        print("Double executed")

    def surrender(self):
        print("Surrender executed")

    def split(self):
        print("Split executed")

    def insurance(self):
        print("Insurance executed")



def main():
    test_player = Player()
    print(test_player.hand)
    print(test_player.dealer_hand)


if __name__ == "__main__":
    main()