import deck
import setup
class Player:
    def __init__(self):
        self.hand = setup.Setup().deal_hand()


def main():
    test_player = Player()
    print(test_player.hand)


if __name__ == "__main__":
    main()