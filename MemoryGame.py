import random
import time
import re
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play(difficulty):
    generate_sequence1 = generate_sequences(difficulty)
    get_list_from_user1 = get_list_from_user(difficulty)
    answer = is_list_equal(generate_sequence1, get_list_from_user1)
    return answer


def generate_sequences(difficulty):
    list_of_number = range(1, 101)
    generate_sequence = str(random.sample(list_of_number, difficulty))
    generate_sequence2 = re.sub(r'[(){}[\]]', '', generate_sequence)
    print(f"The list of number is {generate_sequence2}")
    time.sleep(0.7)
    print(f"Time is up!")
    clear_screen()
    return generate_sequence2


def get_list_from_user(difficulty):
    print(f'\nwrite the same list of {difficulty} numbers with  "," between them:')
    get_list_from_user1 = str(input())
    return get_list_from_user1


def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False
