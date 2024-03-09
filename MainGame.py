import GuessGame
import CurrencyRouletteGame
import MemoryGame
import time
import Score


def welcome():
    print(f"Hello what is your name:\n")
    name = input()
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
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
        won_lost = MemoryGame.play(difficulty)
        Score(difficulty)
        return won_lost
    elif game == 2:
        won_lost = GuessGame.play(difficulty)
        return won_lost
    else:  # game == 3:
        won_lost = CurrencyRouletteGame.play(difficulty)
        return won_lost


welcome()
won_lost = load_game()


def display_won_lost(won_lost, difficulty):
    if won_lost:
        Score.add_score(difficulty)
    else:
        print(f'User Lost')

#
# Display_won_lost(won_lost, difficulty)
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
