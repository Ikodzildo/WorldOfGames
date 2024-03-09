# class Guessgame(difficulty):
import random


def play(difficulty):
    secret_number = random.randint(1, difficulty)
    print(f'choose a number between 1 and {difficulty}')
    get_guess_from_user = int(input())
    answer = compare_results(secret_number, get_guess_from_user)
    # if answer:
    #     print(f' User Won')
    # else:
    #     print(f' User Lost')
    return answer


def compare_results(secret_number, get_guess_from_user):
    if secret_number == get_guess_from_user:
        return True
    else:
        return False
