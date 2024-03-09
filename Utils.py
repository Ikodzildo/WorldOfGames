import os

with open("Scores.txt", "a+") as f:
    f.write("new line\n")

# BAD_RETURN_CODE

def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
