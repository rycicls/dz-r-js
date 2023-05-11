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
        self.curr_player = 0
        self.next_player = self.curr_player + 1
        self.players = []
        self.player_cards = []
        for i in range(player_count):
            self.players.append(Player(i))

    def player_decks(self):
        for self.players in player_count:
            for c in range(self.card_count):
                self.player_cards.append(sd.shufel_deck(c))
                c += 1

class Deck:
    def __init__(self):
        self.deck_list = []
        self.card_count = 52 // player_count
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol,number))
        
    def shuffle_deck(self):
        random.shuffle(self.deck_list)

    def print_deck(self,deck):        
        for card in deck:
            print(f'symbol: {card.symbol}')
            print(f'value: {card.number}')

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck

sd = Deck()
print(f"shuffeled deck: {sd.print_deck(sd.shuffle_deck())}")
# print(f"player name list: {gm.players()}")