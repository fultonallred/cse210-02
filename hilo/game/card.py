import random

class Card:
    '''Represents a drawn card that could have 13 different values.
    
    This object keeps track of the value of the drawn card. 
    
    Attributes: 
        value (int): The number shown on the drawn card.'''

    
    def __init__(self):
        self.value = 0

    def draw_card(self):
        self.value = random.randint(1,13)