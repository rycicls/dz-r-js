import random
from player_count import players_num

symbols = ("clubs", "spades", "hearts", "diamonds")
numbers = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")
jack_value = 11
queen_value = 12
king_value = 13
ace_value = 14

class Card:
    def __init__(self, cardSymbol, cardNumber):
        self.symbol = cardSymbol
        self.number = cardNumber

player_count = players_num()

class Player:
    def __init__(self,name):
        self.name = name

class Deck:
    def __init__(self):
        self.deck_list = []
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol, number))
    
    def shufel_deck(self):
        self.shufeled_deck = random.shuffle(self.deck_list)
        print(self.shufeled_deck)

    def deal_decks(self):
        self.player1_deck = []

sd = Deck
sd.shufel_deck
print(f"shuffeled deck: {sd.shufel_deck}")