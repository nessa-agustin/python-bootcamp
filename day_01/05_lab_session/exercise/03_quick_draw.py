from random import choice
# TODO: Ask the user for an input
user_choice = input("Pick a choice (rock/paper/scissors): ")
print('User: ', user_choice)

# TODO: Make a random choice for the computer
# Note: Read the slide for this part
options = ['rock', 'paper', 'scissors']
cpu_choice = choice(options)
print('CPU choice: ', cpu_choice)

# TODO: Determine if the user wins, the cpu wins, or its a draw

def get_results(user_hand, cpu_hand):
    result = None
    if user_choice == cpu_choice:
        result = 'DRAW'
    if user_choice == 'rock' and cpu_choice == 'scissors':
        result = 'USER'
    if (user_choice == 'paper' and cpu_choice == 'scissors') or (user_choice == 'scissors' and cpu_choice == 'rock'):
        print('You lose!')

    return result


# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds

"""
ROCK BEATS SCISSORS
SCISSORS BEATS PAPER
PAPER BEATS ROCK
"""


