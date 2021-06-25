import os
import random

def get_random_word():
    # Get all words from file
    words = []
    with open("./data.txt","r") as f:
        for line in f:
            words.append(line.strip())

    # Get a random word
    random_index = random.randint(0, len(words))

    return words[random_index]


def get_filled_word(challenge_word, user_input):
    cw_list = list(challenge_word)
    user_input_set = set(user_input)
    filled_word = ''
    for letter in cw_list:
        if letter in user_input_set:
            filled_word = filled_word + ' ' + letter
        else:
            filled_word = filled_word + ' _'

    return filled_word

def get_left_attempts(challenge_word, user_input, allowed_failed_attempts):
    # calculate left attempts
    left_attempts = (len(challenge_word) + allowed_failed_attempts) - len(user_input)

    return left_attempts


def check_challenge_done(challenge_word, user_input):
    # Check if challenge is completed
    cw_set = set(list(challenge_word))
    ui_set = set(user_input)

    # if challenge word is a subset of user input the challenge is completed
    return cw_set.issubset(ui_set)

def main():
    # Set challenge configuration
    allowed_failed_attempts = 5

    # Init user input array to store letters selected by user
    user_input = []

    # Get a random word to use as challenge to user guessing
    challenge_word = get_random_word()

    # Check if challenge is completed by user
    challenge_continues = True
    while challenge_continues:
        # Clear screen
        os.system('clear')

        # Calculate challenge word with user input matches in order to show progress
        print(get_filled_word(challenge_word=challenge_word, user_input=user_input))
        user_guess = input('Enter your next letter: ')

        # Add user input to list which is used to check challenge completion and record all user inputs
        user_input.append(str(user_guess))

        # Calculate if game is over by checking if challenge is done and # of failed attempts left
        challenge_done = check_challenge_done(
                challenge_word=challenge_word, 
                user_input=user_input)
        left_attempts = get_left_attempts(
                challenge_word=challenge_word,
                user_input=user_input,
                allowed_failed_attempts=allowed_failed_attempts)

        challenge_continues = (not challenge_done) and (left_attempts > 0)

    # When game is over is presented to user the final progress, and evaluated result of challenge
    os.system('clear')
    print(get_filled_word(challenge_word=challenge_word, user_input=user_input))

    if check_challenge_done(
            challenge_word=challenge_word, 
            user_input=user_input):
        print('Congratulations, You Win!')
    else:
        print('Nice try!, the word was: {}'.format(challenge_word))

if __name__ == '__main__':
    main()

