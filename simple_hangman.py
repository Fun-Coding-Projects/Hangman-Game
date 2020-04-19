#!/usr/bin/env python3.8
'''
Hangman Game by Simon Holland / Inyoka (Basic)
'''

import random
import os

from levels import level_6 as words

myword = random.choice(words)
game_state = list(reversed(range(0,7)))
guessed_letters = []
wrong_letters = []

def main():

    while not won() and game_state[len(wrong_letters)] != 0:
        clear()
        status()
        myguess = input('Enter a letter : ').lower()
        guess(myguess)

    if won():
        clear()
        print(f'Congratulations, you won! The word was "{myword.upper()}"')
        status()

    else :
        clear()
        print(f'Sorry the word was {myword.upper()}')
        status()


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


def status():
    print(f'Guesses left : {game_state[len(wrong_letters)]}')
    print(f'Remaining : {hide_letters(myword)}')


if __name__ == '__main__':
    main()
