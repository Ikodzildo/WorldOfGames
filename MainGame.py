import GuessGame
import CurrencyRouletteGame
import MemoryGame
import time


# import Score


def welcome():
    print(f"Hello what is your name:\n")
    name = input()
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game(a, b):
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    game = int(input())
    print("Please choose game difficulty from 1 to 5:\n")
    difficulty = int(input())
    print(f"You choose game: {game} with level: {difficulty}\n")
    time.sleep(2)

    if game == 1:
        iswon = MemoryGame.play(difficulty)
        return iswon, difficulty
    elif game == 2:
        iswon = GuessGame.play(difficulty)
        return iswon, difficulty
    else:  # game == 3:
        iswon = CurrencyRouletteGame.play(difficulty)
        return iswon, difficulty


def main():
    welcome()
    load_game(a, b)


def display_won_lost(won_lost):
    if won_lost:
        print(f'User won')
        # Score.add_score(difficulty)

    else:
        print(f'User Lost')


display_won_lost(won_lost)
#
#
# answer = 'y'
# while answer == 'y' or answer == 'Y':
#     print(f'Do you want to play another game?(y/n)')
#     answer = input()
#     print(f'Answer is:{answer}')
#     MemoryGame.clear_screen()
#     if answer == 'y':
#         won_lost = load_game()
#         Display_won_lost(won_lost)
#     else:
#         print(f'Bye Bye')


if __name__ == "__main__":
    main()
