#!/usr/bin/env python
# -*- coding: utf-8 -*-

import secrets
from .wordlist import Wordlist

def random_generator(alt_short_wordlist, short_wordlist):
    dice = 5
    if short_wordlist:
        dice = 4

    wordlist = Wordlist(dice, alt_short_wordlist)
    #As per EFF recomendations, roll a total of 6 times
    password = ' '.join(wordlist.select(random_diceroll(dice)) for i in range(6))
    print(password)

def random_diceroll(dice):
    #Generate n dice rolls
    return ''.join(str(secrets.randbelow(6)+1) for i in range(dice))

def walkthrough(alt_short_wordlist):
    #Help text
    print("Roll five dice (or four for the short wordlist) and enter the result in no particular order")
    print("Then repeat it another five times")

    #Retrieve the first die roll and setup the wordlist
    while True:
        try:
            die = get_die_roll()
            wordlist = Wordlist(len(die), alt_short_wordlist)
            print(wordlist.select(die))
            break
        except KeyError as err:
            print("Please enter a valid number.")
            print(err)

    #As per EFF recomendations roll a total of 6 times, ignoring incorrect values
    die_rolls = 5
    while die_rolls > 0:
        try:
            die = get_die_roll()
            print(wordlist.select(die))
            die_rolls -= 1
        except KeyError:
            print("Please enter a valid number.")

def get_die_roll():
    die = input("Input dice roll: ")
    die = die.replace(" ", "")
    return die
