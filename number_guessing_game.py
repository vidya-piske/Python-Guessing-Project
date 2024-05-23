from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def check_guess(shuffled_list, user_guess):
    if shuffled_list[user_guess] == '0':
        return f"Correct! The list was: {shuffled_list}"
    else:
        return f"Wrong guess. The list was: {shuffled_list}"

# Initialization
mylist = ['', '0', '']
