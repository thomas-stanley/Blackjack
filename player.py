import setup
import main
import deck
class Player:
    def __init__(self):
        self.total = 0
        self.current_game = main.Blackjack()
        self.hand = setup.Setup().deal_hand()
        self.dealer_hand = self.current_game.current_dealer.hand
        self.current_deck = deck.Deck()
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
    

    def info_text(self):
        print(f"Dealer's hand: {self.dealer_hand[0]}")
        print(f"Dealer's total: {self.current_game.current_dealer.total}")
        hand_to_print = ", ".join(map(str, self.hand))
        print(f"Current hand: {hand_to_print}")
        print(f"Total: {self.total}")
        print("Choose an action: ")
        for option in self.user_options:
            print(option.capitalize())
        print("-----")

    def keep_total(self):
        self.total = sum([card.value for card in self.hand])

    def action(self) -> str:
        self.keep_total()
        valid_choice = False
        self.info_text()
        while not valid_choice:
            user_choice = input().lower()
            if user_choice in self.user_options:
                valid_choice = True
            else:
                print("Invalid choice. Please try again.")
        self.user_options[user_choice]()
    
    def hit(self):
        self.hand.append(self.current_deck.deal())

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



def run_main():
    test_player = Player()
    print(test_player.hand)
    print(test_player.dealer_hand)


if __name__ == "__main__":
    run_main()