# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:39:20 2018

@author: Daniel
"""

#%%
import random

### lists of suits and ranks of cards, to be dran from later
suits = ['clubs', 'hearts', 'diamonds', 'spades']

ranks = [['two', 2], ['three', 3], ['four', 4], ['five', 5], 
            ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9], ['ten', 10], 
            ['king', 10], ['queen', 10], ['jack', 10], ['ace', 0]]

### a running deck of drawn cards, to ensure no card is repeated
game_deck = []

### the pot containing bet chips
game_pot = 0

#%%

class Card:

    def __init__ (self, suit, rank):

        self.suit = suit
        self.rank = rank


#%%

### the PLayer class is defined with a value of chips, a list of drawn cards,
### and the total value of the cards they hold

class Player:
    
    def __init__(self, chips, hand, hand_value):
        
        self.chips = chips
        self.hand = hand
        self.hand_value = hand_value

### the bet function allows the player to bet amount of chips greater than
### 0 and less than their total amount of chips

    def bet(self):
        
        global game_pot
        global game_deck
        
        print(f'you have {player1.chips} chips.')
        
        query = 1
        while query == 1:
            try:
                bet_amount = int(input('How much would you like to bet? '))
            except:
                print('please enter a number')
                continue
            else:
                if bet_amount > 0 and bet_amount <= self.chips:
                    self.chips = (self.chips - bet_amount)
                    game_pot += bet_amount*2
                    print(f'you wagered {bet_amount} chips; you have {self.chips} chips remaining')
                    print(f'there is {game_pot} chips to be won')
                    print(game_pot)
                    query = 0
                else:
                    print('that is an invalid wager')
        
        self.start()
    
### the start function draws two cards for the player/dealer, then checks the
### total against the win conditions. if the total is not 21, the player is
### given the option to hit or declare
    
    def start(self):
        
        global game_deck
        global game_pot
        
        y = 0
        while y < 2:
            x = 1
            while x == 1:
                new_card = Card(random.choice(suits), random.choice(ranks))
                temp_value = (new_card.suit, new_card.rank)
                if temp_value not in game_deck:
                    x = 0
            
            game_deck.append(temp_value)
            ace_check(temp_value)
            self.hand.append(temp_value)
            self.hand_value += temp_value[1][1]
            print(f'you drew the {new_card.rank[0]} of {new_card.suit}')
            print(f'your hand is worth {self.hand_value}')
            print('your hand contains:')
            for i in range(len(self.hand)):
                print(f'{self.hand[i][1][0]} of {self.hand[i][0]}')
            print("*****")
            y += 1
            
        self.win_check()
        
### the draw function adds one card to the players hand by randomly picking a
### suit and a rank from the pre-defined lists, and checking that selection
### against the list of previously drawn cards to ensure that the combination
### has not been drawn before
                  
    def draw(self):
        
        global game_pot
        global game_deck
        
        x = 1
        while x == 1:
            new_card = Card(random.choice(suits), random.choice(ranks))
            temp_value = (new_card.suit, new_card.rank)
            if temp_value not in game_deck:
                x = 0
        
        game_deck.append(temp_value)
        ace_check(temp_value)
        self.hand.append(temp_value)
        self.hand_value += temp_value[1][1]
        print(f'you drew the {new_card.rank[0]} of {new_card.suit}')
        print(f'your hand is worth {self.hand_value}')
        print('your hand contains:')
        for i in range(len(self.hand)):
            print(f'{self.hand[i][1][0]} of {self.hand[i][0]}')
        print("*****")
        self.win_check()

### wincheck checks the total of the players cards, declares whether the player
### has won, bust, or gives them the option to hit or declare
        
    def win_check(self):
        
        global game_pot
        global game_deck
        
        print(game_pot)
        if self.hand_value == 21:
            self.chips += game_pot
            game_pot = 0
            print(f'congratulations, you won the hand! you now have {self.chips} chips')
            play_again()
        if self.hand_value > 21:
            game_pot = 0
            print('BUST!')
            play_again()
        if self.hand_value < 21:
            query = input('would you like to hit or declare? h/d ')
            if query.lower() == 'd':
                print(f'your total is {player1.hand_value}. It is now the dealers turn')
                print("*****")
                dealer1.start()
            elif query.lower() == 'h':
                self.draw()
                
#%%

### similar to thr player class, the dealer is defined with a hand and a hand
### value

class Dealer:
    
    
    def __init__ (self, hand, hand_value):
        
        self.hand = hand
        self.hand_value = hand_value
        
### the dealer.start function draws two cards for the dealer, then checks it
### against the players hand. if it is worth more than the players and less
### than or equal to 21, the dealer wins        
        
    def start(self):
        
        global game_pot
        global game_deck
        
        print(game_pot)
        
        y = 0
        while y < 2:
            x = 1
            while x == 1:
                new_card = Card(random.choice(suits), random.choice(ranks))
                temp_value = (new_card.suit, new_card.rank)
                if temp_value not in game_deck:
                    x = 0
            game_deck.append(temp_value)
            ace_check(temp_value)
            self.hand.append(temp_value)
            self.hand_value += temp_value[1][1]
            print(f"**the dealer drew the {new_card.rank[0]} of {new_card.suit}")
            print(f"the dealer's hand is worth {self.hand_value}")
            print("the dealer's hand contains:")
            for i in range(len(self.hand)):
                print(f'{self.hand[i][1][0]} of {self.hand[i][0]}')
            print("*****")
            y+=1
        if self.hand_value > player1.hand_value:
            print('the dealer wins!')
            game_pot = 0
        else:
            self.draw()

### while the dealers hand is worth less than the players hand, the draw
### function will draw cards until it is worth more than the players, and then
### check whether the dealer wins or loses
    
    def draw(self):
        
        while self.hand_value <= player1.hand_value:
            x = 1
            while x == 1:
                new_card = Card(random.choice(suits), random.choice(ranks))
                temp_value = (new_card.suit, new_card.rank)
                if temp_value not in game_deck:
                    x = 0
            
            game_deck.append(temp_value)
            ace_check(temp_value)
            self.hand.append(temp_value)
            self.hand_value += temp_value[1][1]
            print(f"the dealer drew the {new_card.rank[0]} of {new_card.suit}")
            print(f"the dealer's hand is worth {self.hand_value}")
            print("the dealer's hand contains:")
            for i in range(len(self.hand)):
                print(f'{self.hand[i][1][0]} of {self.hand[i][0]}')
            print("*****")
        self.win_check()
        
    def win_check(self):
        
        global game_pot
        global game_deck
        
        print(game_pot)
        
        
        if self.hand_value <= 21:
            print('the dealer wins!')
            game_pot = 0
            play_again()
        elif self.hand_value > 21:
            print(f'congratulations, you beat the dealer. you win {game_pot} chips!')
            player1.chips += game_pot
            game_pot = 0
            play_again()
#%%

def ace_check(card):
    
### if the card drawn is an ace, the ace check function allows the player to
### decide its value then adjusts it accordingly
    
    if card[1][0] == 'ace':
        print(f'you drew the ace of {card[0]}')
        check = 0
        while check == 0:
            try:
                
                ace_value = int(input('would you like the ace value to be 1 or 11? '))
            except:
                print('please enter an either 1 or 11')
                continue
            else:
                if ace_value == 1 or ace_value == 11:
                    card[1][1] = ace_value
                    check = 1
                else:
                    print('please enter 1 or 11')

#%%
                    
def game_start():
    
    global player1
    global dealer1
    
    player1 = Player(100, [], 0)
    dealer1 = Dealer([], 0)
    
    print(f'welcome to the blackjack table. you are playing against the dealer and you start with {player1.chips} chips.')
    
    player1.bet()
    
#%%

def play_again():

### resets game values and asks the player if they would like to play again
    
    global game_pot
    global game_deck
    
    game_deck = []
    game_pot = 0
    player1.hand = []
    player1.hand_value = 0
    dealer1.hand = []
    dealer1.hand_value = 0
    
    print(f'you have {player1.chips} remaining; would you like to play another hand?')
    
    if player1.chips == 0:
        print('sorry you are out of chips. you must leave the table.')

    elif player1.chips >= 1:
        x = 0
        while x == 0:
            query = input('play again? y/n')
            if query.lower() == 'y':
                player1.bet()
            elif  query.lower() == 'n':
                print(f'you finished with {player1.chips} chips. thank you for playing.')
                x = 1
            else:
                print('please enter y or n')
                continue
#%%
        
game_start()
        