from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def get_user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Enter a value 0, 1, 2: ")
    return int(guess)

def check_guess(shuffled_list, user_guess):
    if shuffled_list[user_guess] == '0':  
        print(f"Correct value: {shuffled_list}")
    else:
        print(f"Wrong value: {shuffled_list}")

# Initialization
mylist = ['', '0', '']

