
import random

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker
    
    def __str__(self):
        return self.marker
    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker
    
    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {
            key: Square() for 
             key in range(1, 10)
        }
        
    def is_full(self):
        return len(self.unused_squares()) == 0
    
    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()
    
    def unused_squares(self):
        return [key for key, square in self.squares.items() if 
                square.is_unused()]
    
    def is_square_unused(self, key):
        return self.squares[key].is_unused()
    
    
    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)



class Player:

    
    def __init__(self, marker):
        self._marker = marker
        self._score = 0
        self.game_winner = None
    
    @property
    def score(self):
        return self._score

    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, value):
        self._marker = value
    
    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative.")
        self._score = value
    
    def increment_score(self):
        self.score += 1


class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:

    MATCH_GOAL = 3

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )
    
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
    
    def play(self):
        self.display_welcome_message()
        while True:
            self.play_one_game()
            if self.player_won_three_times(self.human):
                print("You won the match! Congratulations")
                if not self._playAgain():
                    break
            
            elif self.player_won_three_times(self.computer):
                print("I won the match!  Take that human!")
                if not self._playAgain():
                    break
            
        self.display_goodby_message
    
    def detect_winner(self):

        if self.is_winner(self.human):
            self.human.increment_score()
            self.game_winner = self.human
            print(f"Human's win total is now {self.human.score}")
            print(f"Computer's win total is now {self.computer.score}")
        
        if self.is_winner(self.computer):
            self.computer.increment_score()
            self.game_winner = self.computer
            print(f"Human's win total is now {self.human.score}")
            print(f"Computer's win total is now {self.computer.score}")
    

    def play_one_game(self):
        
        self.board = Board()
        while True:
            self.board.display()
            if self.game_winner == self.computer or self.game_winner == None:
                self.human_moves()
                if self.is_game_over():
                    self.board.display()
                    self.display_results()
                    self.detect_winner()
                    break
                    

                self.computer_moves()
                if self.is_game_over():
                    self.board.display()
                    self.display_results()
                    self.detect_winner()
                    break
            else:

                self.computer_moves()
                if self.is_game_over():
                    self.board.display()
                    self.display_results()
                    self.detect_winner()
                    break

                self.human_moves()
                if self.is_game_over():
                    self.board.display()
                    self.display_results()
                    self.detect_winner()
                    break


    
    def is_game_over(self):
        return self.board.is_full() or self.someone_won()
    
    def player_won_three_times(self, player):
        return player.score >= TTTGame.MATCH_GOAL

    
    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that human")
        else:
            print("A tie game. How boring.")
    
    def three_in_a_row(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if all(self.board.squares[key].marker == player.marker for key in row):
                return True
        return False
        
    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player):
                return True
            
        return False
    
    @staticmethod
    def _join_or(items, delimiter=', ', final_delimiter=' or '):
        if len(items) == 1:
            return items[0]
        elif len(items) == 2:
            return f"{items[0]}{final_delimiter}{items[1]}"
        else:
            return f"{delimiter.join(items[:-1])}{final_delimiter}{items[-1]}"
    
    
    def _playAgain(self):
        answer = input("Would you like to play again? (y/n): ")
        if answer not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'")
            return self._playAgain()
        elif answer == 'y':
            print('Starting a new game.')
            self.board = Board()
            self.human.score = 0
            self.computer.score = 0
            return True
        else:
            self.display_goodbye_message()
            return False
       
          

    
    def human_moves(self):
        valid_choices = self.board.unused_squares()
        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            prompt = f"Choose a square between {choices_str}: "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()
        self.board.mark_square_at(choice, self.human.marker)
    
    def check_for_two_of_three(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2 and \
               any(self.board.is_square_unused(key) for key in row):
                return True
        return False
    
    def choose_ai_move(self):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(self.computer, row) == 2 and \
                any(self.board.is_square_unused(key) for key in row):
                return next(key for key in row if self.board.is_square_unused(key))
            elif self.board.count_markers_for(self.human, row) == 2 and \
               any(self.board.is_square_unused(key) for key in row):
                return next(key for key in row if self.board.is_square_unused(key))

    
    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        if self.check_for_two_of_three(self.computer) or self.check_for_two_of_three(self.human):
            choice = self.choose_ai_move()
            print("Computer moves")
            self.board.mark_square_at(choice, self.computer.marker)
        
        
        elif self.board.is_square_unused(5):
            choice = 5
            print("Computer moves")
            self.board.mark_square_at(choice, self.computer.marker)

        else:
            choice = random.choice(valid_choices)
            print("Computer moves")
            self.board.mark_square_at(choice, self.computer.marker)
    
    def is_game_over(self):
        return self.board.is_full() or self.someone_won()
    
    
    
    
    def someone_won(self):
        return (self.is_winner(self.human)
                or self.is_winner(self.computer))

game = TTTGame()
game.play()

