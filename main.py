import random
from player_count import players_num

symbols = ("clubs", "spades", "hearts", "diamonds")
numbers = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")
jack_value = 11 #values for cards others will look at number
queen_value = 12
king_value = 13
ace_value = 14

class Card:
    def __init__(self, cardSymbol, cardNumber):
        self.symbol = cardSymbol
        self.number = cardNumber

player_count = players_num() #gonna be visual curently asks how many players with cmd

class Player:
    def __init__(self,player_name):
        self.player_name = player_name
        self.player_cards = []
        for c in range(sd.cards_per_deck):
            self.player_cards.append(sd.shufel_deck(c))
            c += 1

class Deck:
    def __init__(self):
        self.deck_list = []

    def make_deck(self):
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol,number))
        # return self.deck_list()
        
    
    def shufel_deck(self):
        random.shuffle(self.deck_list)
        return self.deck_list #returns none

    def deal_decks(self):
        self.cards_per_deck = 52 / player_count

    def print_deck(self,deck):        
        for card in deck:
            print(f'symbol: {card.symbol}')
            print(f'value: {card.number}')

class Game:
    def players_names(self):
        self.players = []
        for i in range(player_count):
            self.players.append(Player(i))

pl = Player()
sd = Deck()
print(f"player name list: {pl.give_names()}")
print(f"deck: {sd.make_deck()}") #testing
print(f"shuffeled deck: {sd.print_deck(sd.shufel_deck())}")
