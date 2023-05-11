import random

symbols = ("clubs", "spades", "hearts", "diamonds")
numbers = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J': 11,'Q': 12,'K': 13,'A': 14}
jack_value = 11 #values for cards others will look at number
queen_value = 12
king_value = 13
ace_value = 14

def players_num(): #plan to make visual with pysimpleGUI
    print("how many players: ")
    player_count_input = input()
    player_count_input = int(player_count_input)
    if player_count_input > 52:
        print(f'too many players. Need to be less than 52')
        exit
    print(f"entered players: {player_count_input}")
    return player_count_input

player_count = players_num() #gonna be visual curently asks how many players with cmd

class Card:
    def __init__(self, cardSymbol, cardNumber):
        self.symbol = cardSymbol
        self.number = cardNumber

class Deck:
    def __init__(self):
        self.deck_list = []
        for symbol in symbols:
            for number in numbers:
                self.deck_list.append(Card(symbol,number))

    def shuffle(self):
        random.shuffle(self.deck_list)
        return self.deck_list
    
    def deal(self):
        return self.deck_list.pop()
    
    def print_deck(self,deck):
        for card in deck:
            print(f'symbol: {card.symbol}')
            print(f'value: {card.number}')

deck = Deck()

class Player:
    def __init__(self,name):
        self.player_name = name
        self.player_deck = []

    def add_card(self,card):
        self.player_deck.append(card)
    
    def remove_card(self,card):
        self.player_deck.remove(card)

    def print_hand(self):
        for card in self.player_deck:
            print(card)

class Game:
    def __init__(self):
        self.player = Player("vards")
        self.deck = Deck()
        self.deck.shuffle()
        self.card_count = 52 // player_count
        self.players = []
        for i in range(player_count):
            self.players.append(Player(i))

    def deal_cards(self):
        k = 0
        for k in range(self.card_count):
            for Player in self.players:
                Player.add_card(self.deck.deal())
            k += 1
    
    def play(self):
        self.deal_cards()
        self.curr_player = 0
        print(f'player count: {player_count}')
        for j in range(random.randint(10000000000000,9999999999999999999)):
            self.next_player = self.curr_player + 1
            print(f'next ply: {self.next_player}')
            print(f'curr ply: {self.curr_player}')
            if self.next_player > player_count:
                self.next_player = 0
            if self.curr_player > player_count:
                self.curr_player = 0
            print(f'move:')
            played_cards = []
            played_cards.append(self.players[self.curr_player].player_deck[0])
            # print(self.players[self.curr_player].player_deck)
            Player.remove_card(self.players[self.curr_player],self.players[self.curr_player].player_deck[0])
            played_cards.append(self.players[self.next_player].player_deck[0])
            Player.remove_card(self.players[self.next_player],self.players[self.next_player].player_deck[0])
            if played_cards[0].number > played_cards[1].number:
                Player.add_card(self.players[self.curr_player],played_cards)
                # self.players[self.curr_player].player_deck.append(played_cards)
                print(f'player {self.players[self.curr_player].player_name} won')
                # break
            elif played_cards[0].number > played_cards[1].number:
                Player.add_card(self.players[self.next_player],played_cards)
                # self.players[self.next_player].player_deck.append(played_cards)
                print(f'player {self.players[self.next_player].player_name} won')
                # break
            elif played_cards[0].number == played_cards[1].number:
                print(f'both cards are of equal value')
                continue
            
            self.curr_player += 1
            # self.next_player += 1
            j += 1
     
game = Game()
game.play()