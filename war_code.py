import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'J', 'Q', 'K', 'A']
    values = {rank: i+2 for i, rank in enumerate(ranks)}  # 2=2, ..., A=14

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class StandardDeck:
    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in Card.suits
                      for rank in Card.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0) if self.cards else None


class WarGame:
    def __init__(self):
        deck = StandardDeck()
        # Split deck in half
        self.player1 = deck.cards[:26]
        self.player2 = deck.cards[26:]

    def play_round(self):
        if not self.player1 or not self.player2:
            return False  # Game ends

        card1 = self.player1.pop(0)
        card2 = self.player2.pop(0)

        print(f"Player 1 plays: {card1}")
        print(f"Player 2 plays: {card2}")

        if card1.value > card2.value:
            print("Player 1 wins this round!\n")
            self.player1.extend([card1, card2])
        elif card2.value > card1.value:
            print("Player 2 wins this round!\n")
            self.player2.extend([card1, card2])
        else:
            print("It's a tie! Both cards are discarded.\n")
           
        return True

    def play_game(self):
        round_num = 1
        while self.player1 and self.player2:
            print(f"--- Round {round_num} ---")
            self.play_round()
            round_num += 1

        if self.player1:
            print("Player 1 WINS the game! 🎉")
        else:
            print("Player 2 WINS the game! 🎉")



if __name__ == "__main__":
    game = WarGame()
    game.play_game()
