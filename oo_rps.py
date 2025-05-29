import random
import numpy as np


class History:
    def __init__(self):
        self.value = []
    
    def add_move(self, move):
        if isinstance(move, Move):
            self.value.append(move)
            out_history = " ".join(str(val) for val in self.value)
            print(out_history)
        else:
            return NotImplemented

class Move: 
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.value == other.value
        return NotImplemented


class Rock(Move):
    def __init__(self):
        super().__init__('rock')
    
    
    def beats(self, other):
        return str(other) in ['scissors', 'lizard']

class Paper(Move):
    def __init__(self):
        super().__init__('paper')
    
    
    def beats(self, other):
        return str(other) in ['rock', 'spock']

class Scissors(Move):
    def __init__(self):
        super().__init__('scissors')
    
    
    def beats(self, other):
        return str(other) in ['paper', 'lizard']

class Lizard(Move):
    def __init__(self):
        super().__init__('lizard')
    
    
    def beats(self, other):
        return str(other) in ['paper', 'spock']

class Spock(Move):
    def __init__(self,):
        super().__init__('spock')
    
    
    def beats(self, other):
        return str(other) in ['rock', 'scissors']
    
class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    MOVE_CLASSES = {
        'rock': Rock,
        'paper': Paper,
        'scissors': Scissors,
        'lizard': Lizard,
        'spock': Spock
    }

    def __init__(self):   
        self.move = None
        self.history = History()

class Score:
    def __init__(self):
        self.points = 0
    
    def increment_score(self):
        self.points += 1
    
    
    def __str__(self):
        return str(self.points)

    
class Computer(Player, Score):
    
    def __init__(self):
        super().__init__()
        self.score = Score()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self.move = Player.MOVE_CLASSES[choice]()
        self.history.add_move(self.move)


class Daneel(Computer):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        if bool(self.history) == False:
            
            choice = random.choice(Player.CHOICES)
            self.move = Player.MOVE_CLASSES[choice]()
            self.history.add_move(self.move)
        else:
            self.move = self.history.value[0]()
            self.history.add_move(self.move)


class R2d2(Computer):
    def __init_(self):
        super.__init__()
    
    def choose(self):
        self.move = Rock()
        self.history.add_move(self.move)

class Hal(Computer):
    def __init__(self):
        super.__init__()
    
    def choose(self):
        probabilities = [.1, .1, .6, .1, .1]
        choice = np.random.choice(Player.CHOICES, p=probabilities)
        self.move = Player.MOVE_CLASSES[choice]()
        self.history.add_move(self.move)
        



class Human(Player, Score):

    def __init__(self):
        super().__init__()
        self.move = None
        self.score = Score()

    def choose(self):
        prompt = 'Please choose rock, paper, scissors, lizard, or spock:'

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = Player.MOVE_CLASSES[choice]()
        self.history.add_move(self.move)
    
    

class RPSGame:

    PERSONALITY_LIST = ['daneel', 'r2d2', 'hal']
    PERSONALITY_CLASSES = {
        'daneel': Daneel,
        'r2d2': R2d2,
        'hal': Hal

    }
    

    
    def __init__(self):
        self._human = Human()
        choice = random.choice(self.PERSONALITY_LIST)
        self._computer = self.PERSONALITY_CLASSES[choice]()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard spock!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return human_move.beats(computer_move)

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return computer_move.beats(human_move)

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            self._human.score.increment_score()
            print(self._human.score)
            print(self._computer.score)
            print('You win!')
        elif self._computer_wins():
            print('Computer Wins!')
            self._computer.score.increment_score()
            print(self._human.score)
            print(self._computer.score)

        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')
    


    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if self._human.score.points == 5 or self._computer.score.points == 5:
                if not self._play_again():
                    self._display_goodbye_message()
                    break

RPSGame().play()
