from UNO import hand, deck, card, uno
from TicTacToe import TicTacToe_AI as TTT
from RPS import rps
from Hangman import hangman

PROJECT_NAME = "Kyle's Game Collection"

READABLE_GAME_NAMES = {"uno": "UNO",
                       "TTT": "Tic Tac Toe",
                       "rps": "Rock Paper Scissors",
                       "hangman": "Hangman"}

# uno, tic tac toe, fireball, hangman, rock paper scissors

def option_formatter(choice):
    try:
        choice = int(choice)
    except ValueError:
        pass

    if isinstance(choice, str):
        choice = choice.lower()

    return choice


def prompt(game: str):
    print(f"You selected: {READABLE_GAME_NAMES[game]}\n")
    while True:
        print("1. Play Game\n2. Rules\n3. Back")
        option = option_formatter(int(input("Choose an option: ")))
        print()

        if option == 1:
            print("Starting Game... Have Fun!")
            return eval(game).play_game()
        elif option == 2:
            eval(game).print_rules()
        else:
            return False


print(f"Welcome to {PROJECT_NAME}!\n")

while True:
    print("1. UNO\n2. Tic Tac Toe\n3. Rock Paper Scissors\n4. Hangman")

    game = option_formatter(input("Pick a game to play: "))
    if game in (1, "uno"):
        if not prompt("uno"):
            continue

    elif game in (2, "tic tac toe", "ttt", "tictactoe"):
        if not prompt("TTT"):
            continue

    elif game in (3, "rps", "rock paper scissors"):
        if not prompt("rps"):
            continue

    elif game in (4, "hangman", "h"):
        if not prompt("hangman"):
            continue


    else:
        print("I couldn't understand that. Try using the game's "
              "numbers? ex. 1 for UNO")
        continue

    ending = input("Thanks for playing! Choose another game? (y/n) ").lower()

    if ending != "y":
        print("Bye!")
        break
