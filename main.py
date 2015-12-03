#!/usr/bin/env python
from card import Card

colors=["red","green","purple"]
shapes=["diamond","squiggle","elipse"]
shades=["solid","shaded","clear"]

def makeDeck(colors,shapes,shades):
    deck=[]
    for color in colors:
        for shape in shapes:
            for shade in shades:
                for num in range(1,4):    
                    deck.append(Card(color,shape,shade,num))
    return deck


if __name__=='__main__':
    deck=makeDeck(colors,shapes,shades)
    print len(deck)
