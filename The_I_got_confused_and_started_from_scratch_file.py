import random
from player_count import players_num

symbols = ("clubs", "spades", "hearts", "diamonds")
numbers = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")
jack_value = 11 #values for cards others will look at number
queen_value = 12
king_value = 13
ace_value = 14

player_count = players_num() #gonna be visual curently asks how many players with cmd

class Card:
    def __init__(self, cardSymbol, cardNumber):
        self.symbol = cardSymbol
        self.number = cardNumber

class Deck:
    def __init__(self):
        self.deck_list = []
    
    def make_deck(self):
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol,number))

    def shuffle(self):
        random.shuffle(self.deck_list)
        return self.deck_list
    
    def print_deck(self,deck):
        for card in deck:
            print(f'symbol: {card.symbol}')
            print(f'value: {card.number}')

deck = Deck()

class Player:
    def __init__(self,name):
            self.player_name = name
            self.card_count = 52 // player_count

plyr = Player()

class Game:
    def __init__(self):
        self.curr_player = 0
        self.players = []
        for i in range(player_count):
            self.players.append(Player(i))

    def give_cards(self):
        for x in range(self.players):
            for card in plyr.card_count:
                pass
        x += 1

    def move(self):
        print(f'type a to make a move')
        player_move = input()
        player_move = str(player_move)
        if player_move == 'a':
            self.next_player = self.curr_player + 1
            print(f'strada')
            self.curr_player += 1
     
game = Game()
game.move()
print(f'shuffled deck: {deck.print_deck(deck.shuffle())}')