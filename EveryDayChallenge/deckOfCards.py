'''Implement Deck of Cards'''

import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for val in range(1,14):
                self.deck.append(Card(val,suit))

    def show(self):
        for card in self.deck:
            card.show()
    
    def shuffle(self):
        for i in range(len(self.deck)-1,-1,-1):
            rand = random.randint(0,i)
            self.deck[rand],self.deck[i] = self.deck[i], self.deck[rand]
        return self.deck
    
    def draw(self):
        if len(self.deck)!=0:
            return self.deck.pop()
        else:
            print('Deck is empty')


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
    
    def showHand(self):
        for card in self.hand:
            card.show()


d1 = Deck()
d1.shuffle()
sandra = Player('Sandra')
sandra.draw(d1)
sandra.showHand()
sandra.draw(d1)
sandra.showHand()