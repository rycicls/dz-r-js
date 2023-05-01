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
    def __init__(self,name):
        self.name = name

class Deck:
    def __init__(self):
        self.deck_list = []

    def make_deck(self):
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol, number))
        return self.deck_list(symbol,number) # makes deck but doesn't show cards
        
    
    def shufel_deck(self):
        self.shufeled_deck = random.shuffle(self.deck_list)
        return self.shufeled_deck #returns none

    def deal_decks(self):
        self.player1_deck = [] #haven't started haven't figured out yet what to do

sd = Deck()
print(f"deck: {sd.make_deck()}") #testing
print(f"shuffeled deck: {sd.shufel_deck()}")