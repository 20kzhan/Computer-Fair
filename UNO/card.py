class Card:
    COLOR = ('RED', 'GREEN', 'BLUE', 'YELLOW')
    RANK = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw2', 'Draw4', 'Wild')
    CTYPE = {'0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number', '6': 'number',
             '7': 'number', '8': 'number', '9': 'number', 'Skip': 'action', 'Reverse': 'action', 'Draw2': 'action',
             'Draw4': 'action_nocolor', 'Wild': 'action_nocolor'}

    def __init__(self, color, rank):
        self.rank = rank
        if self.CTYPE[rank] == 'number':
            self.color = color
            self.cardtype = 'number'
        elif self.CTYPE[rank] == 'action':
            self.color = color
            self.cardtype = 'action'
        else:
            self.color = None
            self.cardtype = 'action_nocolor'

    def __str__(self):
        if self.color is None:
            return self.rank
        else:
            return self.color + " " + self.rank
        
        
if __name__ == "__main__":
    c1 = Card("RED", "Skip")
    print(c1) # this should print a red UNO card 11 (chars across) x 9 (chars vertical) with the text skip on line# 6 (centered)
    
    c2 = Card("BLUE", "Reverse")
    print(c2)
    
    
