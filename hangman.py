#!/usr/bin/env python3.8
'''
Hangman Game by Simon Holland / Inyoka (Advanced)
'''

import random
import os
import re
import time

from levels import level_7 as words
from gallows import gallows


myword = random.choice(words)
game_state = list(reversed(range(0,7)))
guessed_letters, wrong_letters = [], []


def main():
    while not won() and game_state[len(wrong_letters)] != 0:
        run()

    if won():
        clear()
        status()
        print(f'Congratulations, you won! The word was "{myword.upper()}"\n')
    else :
        clear()
        status()
        print(f'Sorry the word was {myword.upper()}\n')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def won():
    if ' _ ' not in hide_letters(myword):
        return True
    return False


def guess(letter):
    if letter in myword and letter not in guessed_letters:
        guessed_letters.append(letter)
    elif letter not in myword and letter not in wrong_letters:
        wrong_letters.append(letter)
    else:
        return False
    return True
    

def hide_letters(word):
    hidden_letters = ''
    for letter in word:
        if letter not in guessed_letters:
            hidden_letters += ' _ '
        else:
            hidden_letters += f' {letter} '
    return hidden_letters


def show_letters(wrong_letters):
    return ', '.join(wrong_letters)


def status():
    print(f'Guesses left : {game_state[len(wrong_letters)]}\n')
    print(f'Mistakes : {show_letters(wrong_letters)}')
    print(gallows[len(wrong_letters)])
    print(f'Remaining : {hide_letters(myword)}\n')


def run():
    clear()
    status()
    myguess = input('Enter a letter : ').lower()
    if re.match('[a-z]', myguess) :
        guess(myguess[0])
    else :
        run()


if __name__ == '__main__':
    main()
