import player
import dealer
class Blackjack:
    def __init__(self):
        self.current_dealer = dealer.Dealer()
        self.current_player = player.Player()
        self.current_player.action()
    

def run_main():
    blackjack = Blackjack()

if __name__ == "__main__":  
    run_main()
