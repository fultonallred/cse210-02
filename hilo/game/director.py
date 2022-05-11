from game.card import Card

class Director:
    '''   
    Attributes:
        card (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.'''

    def __init__(self):
        # We only need one instance per turn so self.card can equal the Card class directly. 
        self.card = Card()
        #A place to hold the last turn's value.
        self.last_value = 0
        #Boolean is true to start the game.
        self.is_playing = True
        #Game points start at 300.
        self.score = 300
        #A place to keep the user input for higher or lower. 
        self.higher_lower = ''

    def start_game(self):
        '''Starts the game and continues the game loop.'''
        while self.is_playing:
            card = self.card
            card.draw_card()
            self.last_value = card.value
            print()
            print(f'The card is {card.value}')

            self.get_higher_lower()
            self.do_updates()
            self.do_outputs()
            
    def get_higher_lower(self):
        '''Asks the user for higher lower chose and records that input.'''
        higher_lower = input('Higher or lower? [h/l]: ')
        self.higher_lower = higher_lower
    
    def do_updates(self):
        '''Draws the next card and updates the play score.'''
        card = self.card
        card.draw_card()
        if card.value > self.last_value and self.higher_lower == 'h':
            self.score += 100
        elif card.value > self.last_value and self.higher_lower == 'l':
            self.score -= 75
        elif card.value < self.last_value and self.higher_lower == 'h':
            self.score -= 75
        elif card.value < self.last_value and self.higher_lower == 'l':
            self.score += 100 

    def do_outputs(self):
        '''Displays the new card value and current score. Also asks user to continue playing and updates boolean for game loop.'''
        card = self.card
        print(f'The next card was {card.value}.')
        print(f'Your score is {self.score}')

        if self.score > 0:
            play_again = input('Play again? [y/n]: ')
            self.is_playing = (play_again == 'y')

        else:
            self.is_playing = False



        