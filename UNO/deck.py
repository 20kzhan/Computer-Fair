from card import Card
import random

class Deck:
    COLOR = ('RED', 'GREEN', 'BLUE', 'YELLOW')
    RANK = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw2', 'Draw4', 'Wild')
    CTYPE = {'0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number', '6': 'number',
             '7': 'number', '8': 'number', '9': 'number', 'Skip': 'action', 'Reverse': 'action', 'Draw2': 'action',
             'Draw4': 'action_nocolor', 'Wild': 'action_nocolor'}

    def __init__(self):
        self.deck = []
        for clr in self.COLOR:
            for ran in self.RANK:
                if self.CTYPE[ran] != 'action_nocolor':
                    self.deck.append(Card(clr, ran))
                    self.deck.append(Card(clr, ran))
                else:
                    self.deck.append(Card(clr, ran))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + str(card)
        return 'The deck has ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()