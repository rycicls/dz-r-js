import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def show_hand(self):
        for card in self.hand:
            print(card)

class Dzeraji:
    def __init__(self, player1, player2):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.players = [self.player1, self.player2]

    def deal_cards(self):
        for i in range(5):
            for player in self.players:
                player.add_card(self.deck.deal())

    def play_game(self):
        print("Let's play Dzērāji!")
        self.deal_cards()
        print(f"{self.player1.name} hand:")
        self.player1.show_hand()
        print(f"{self.player2.name} hand:")
        self.player2.show_hand()

        for i in range(5):
            print(f"Round {i+1}")
            played_cards = []
            for player in self.players:
                print(f"{player.name} turn:")
                selected_card = input("Enter the card you want to play: ")
                selected_card = Card(*selected_card.split())
                played_cards.append(selected_card)
                player.remove_card(selected_card)
                print(f"{player.name} played {selected_card}")
            if played_cards[0].suit == played_cards[1].suit:
                print(f"Matching suit: {played_cards[0].suit}!")
                loser = random.choice(self.players)
                print(f"{loser.name} drinks!")
            else:
                print("No matching suit.")
            print()

        print("Game over!")

if __name__ == '__main__':
    game = Dzeraji("Alice", "Bob")
    game.play_game()
