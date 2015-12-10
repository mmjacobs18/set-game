#!/usr/bin/env python
import copy
import kivy
from card import Card
from random import shuffle
from kivy.app import App
from kivy.uix.label import Label

colors=["red","green","purple"]
shapes=["diamond","squiggle","elipse"]
shades=["solid","shaded","clear"]

def makeDeck(colors,shapes,shades):
#creates and returns the complete deck of 81 cards 
    deck=[]
    for color in colors:
        for shape in shapes:
            for shade in shades:
                for num in range(1,4):    
                    deck.append(Card(color,shape,shade,num))
    return deck

def shuffleDeck(deck):
#returns shuffled deck
    shuffled_deck=copy.deepcopy(deck)
    shuffle(shuffled_deck)
    return shuffled_deck

def isSet(card1,card2,card3):
#returns True if Cards card1, card2, and card3 constitute a set
    color= is_same(card1.color,card2.color,card3.color) or all_different(card1.color,card2.color,card3.color)
    shape=is_same(card1.shape,card2.shape,card3.shape) or all_different(card1.shape,card2.shape,card3.shape)
    shade=is_same(card1.shade,card2.shade,card3.shade) or all_different(card1.shade,card2.shade,card3.shade)
    number=is_same(card1.num,card2.num,card3.num) or all_different(card1.num,card2.num,card3.num)
    return color and shape and shade and number

def is_same(item1,item2,item3):
#returns True if item1, item2, and item3 are the same
    if item1==item2 and item2==item3:
        return True
    else:
        return False

def all_different(item1,item2,item3):
#returns True if item1, item2, and item3 are all different
    if (item1!=item2 and item1!=item3) and item2!=item3:
        return True
    else:
        return False


#############################################################################
if __name__=='__main__':
    deck=makeDeck(colors,shapes,shades)
    sd=shuffleDeck(deck)
#    print isSet(deck[2],deck[5],deck[3])
