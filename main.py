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
        self.card_count = 52 / player_count

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

    def print_deck(self,deck):        
        for card in deck:
            print(f'symbol: {card.symbol}')
            print(f'value: {card.number}')
    
    def player_decks(self):
        self.player_cards = []
        for players in player_count:
            for c in range(self.cards_per_deck):
                self.player_cards.append(sd.shufel_deck(c))
                c += 1

class Game:
    def players_names(self):
        self.players = []
        for i in range(player_count):
            self.players.append(Player(i))

    def move(self):
        self.curr_player = 0
        self.next_player = self.curr_player + 1
        print(f'to make move type a')
        move_input = input()
        move_input = str(move_input)
        if move_input == 'a':
            # if sd.player_cards[0]
            pass

        if self.curr_player < self.player_count - 1:
            self.curr_player = self.curr_player + 1
        else:
            self.curr_player = 0

        if self.next_player < self.player_count - 1:
            self.next_player = self.next_player + 1
        else:
            self.next_player = 0

gm = Game()
# pl = Player()
sd = Deck()
print(f"shuffeled deck: {sd.print_deck(sd.shufel_deck())}")
print(f"player name list: {gm.players_names()}")