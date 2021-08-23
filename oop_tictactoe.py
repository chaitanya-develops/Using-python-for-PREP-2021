# import random
"""TECHNICAL DEBT :
    1)WORK ON WHO GOES FIRST AND LET THE PLAYER CHOOSE LETTERS
    2)WORK OUT ALL EXCEPTIONS ON input
    """
contents = ["invalid index", ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


class Board():
    def __init__(self, contents):
        self.contents = contents

    def display(self):
        print(f"{self.contents[7]} | {self.contents[8]} | {self.contents[9]}")
        print("__|___|__")
        print(f"{self.contents[4]} | {self.contents[5]} | {self.contents[6]}")
        print("__|___|__")
        print(f"{self.contents[1]} | {self.contents[2]} | {self.contents[3]}")

    def get_input_and_update(self, Player):
        while True:
            position = int(
                input(f"{Player.name}, Choose an empty space on the board!!"))
            if self.contents[position] != ' ':
                print("That was not empty, try again.")
                continue
            else:
                self.contents[position] = Player.letter
                break

    def check_win(self, letter):
        return ((self.contents[7] == self.contents[8] == self.contents[9]
                 == letter)
                or (self.contents[4] == self.contents[5] == self.contents[6]
                    == letter)
                or (self.contents[1] == self.contents[2] == self.contents[3]
                    == letter)
                or (self.contents[7] == self.contents[4] == self.contents[1]
                    == letter)
                or (self.contents[8] == self.contents[5] == self.contents[2]
                    == letter)
                or (self.contents[9] == self.contents[6] == self.contents[3]
                    == letter)
                or (self.contents[7] == self.contents[5] == self.contents[3]
                    == letter)
                or (self.contents[9] == self.contents[5] == self.contents[1]
                    == letter))


class Player():
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def __str__(self):
        # This is a placeholder fill this
        return f"{self.name}'s letter is {self.letter}"


# Game Setup
playerOne = Player("PlayerOne", "X")
playerTwo = Player("PlayerTwo", "O")

fresh_board = Board(contents)
game_on = True
turn = 0
while game_on:
    for i in range(1, 10):
        if fresh_board.contents[i] == ' ':
            pass
        else:
            print("That's a draw !!")
            break

    fresh_board.display()
    if turn == 0:
        fresh_board.get_input_and_update(playerOne)
        if fresh_board.check_win(playerOne.letter):
            fresh_board.display()
            print(f"{playerOne.name} Wins!!")
            break
        turn = 1
    else:
        fresh_board.get_input_and_update(playerTwo)
        if fresh_board.check_win(playerTwo.letter):
            fresh_board.display()
            print(f"{playerTwo.name} Wins!!")
            break
        turn = 0
