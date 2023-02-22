path_file = 'src/data/words_frequency.txt'
import random
random.seed(46)

#read file and store 5 letter words in a list
with open(path_file) as f:
    words = [word.strip().split(', ')[0] for word in f]
my_words = []
for word in words:
    if len(word) == 5:
        my_words.append(word)

#import colored function from termcolor module to colorize text
from termcolor import colored

def print_success(text):
    print(colored(text.upper(), 'green', attrs=['reverse']), end='')

def print_warning(text):
    print(colored(text.upper(), 'yellow', attrs=['reverse']), end='')

def print_error(text):
    print(colored(text.upper(), 'red', attrs=['reverse']), end='')

def print_grey(text):
    print(colored(text.upper(), 'grey', attrs=['reverse']), end='')

#main
num_try = 6
guess_word = random.choice(my_words[:10_000])
is_success = False
while num_try:
    user_word = input(f'Enter 5 letter word({num_try} remaining): ')
    if len(user_word) != 5:
        print('The word should have 5 letter!')
        continue
    if user_word not in my_words:
        print('Word not found!')
        continue

    for g_letter, u_letter in zip(guess_word, user_word):
        if g_letter == u_letter:
            print_success(u_letter)
        elif u_letter in guess_word:
            print_warning(u_letter)
        else:
            print_error(u_letter)
    print()
    if user_word == guess_word:
        print()
        print_success('Congratulations!')
        is_success = True
        break
    num_try -= 1

if not is_success:
    print()
    print_error(f'Sorry man game over!!! the word was {guess_word}')
