# Further developments.
# Use gui for displaying the simulation.
# Map the data into visulization and work on the data part.
# Host this as a website that predicts the winner based on user input of Cards.

import random

suits = ("Hearts", "Clubs", "Diamonds", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Jack", "Ten", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
          "Queen": 12, "King": 13, "Ace": 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return f"The number of cards in this deck is {len(self.all_cards)}"

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards"

    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)


# Game setup
player_one = Player("One")
player_two = Player("Two")


fresh_deck = Deck()

fresh_deck.shuffle()


for i in range(26):
    player_one.add_cards(fresh_deck.deal_one())
    player_two.add_cards(fresh_deck.deal_one())

game_on = True
round_num = 0

# Include below commented snippet to print the "inital hands of both Players".
# for i in player_one.cards:
#     print(i, end=' ')
#
# for i in player_two.cards:
#     print(i, end=' ')

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.cards) == 0:
        print(
            f"Player {player_one.name} is out of Cards, Player {player_two.name} Wins.")
        break

    if len(player_two.cards) == 0:
        print(
            f"Player {player_two.name} is out of Cards, Player {player_one.name} Wins.")
        break

#    Start a new round
    player_one_table = []
    player_one_table.append(player_one.remove_one())

    player_two_table = []
    player_two_table.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_table[-1].value > player_two_table[-1].value:

            player_one.add_cards(player_one_table)
            player_one.add_cards(player_two_table)
            print("Player one won the round")

            at_war = False

        elif player_one_table[-1].value < player_two_table[-1].value:

            player_two.add_cards(player_one_table)
            player_two.add_cards(player_two_table)
            print("Player two won the round")

            at_war = False

        else:
            print("WAR!")

            if len(player_one.cards) < 3:
                print("Player One unable to declare War.")
                print("Player Two wins!")
                game_on = False
                break

            elif len(player_two.cards) < 3:
                print("Player Two unable to declare War.")
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_table.append(player_one.remove_one())
                    player_two_table.append(player_two.remove_one())
