import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):   
        pass

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
        self.move = random.choice(Player.CHOICES)

class Human(Player, Score):

    def __init__(self):
        self.move = None
        self.score = Score()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors:'

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice
    
    

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
            (computer_move == 'paper' and human_move == 'rock') or
            (computer_move == 'scissors' and human_move == 'paper'))

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
            self._display_goodbye_message()
            if self._human.score.points == 5 or self._computer.score.points == 5:
                if not self._play_again():
                    break

RPSGame().play()
