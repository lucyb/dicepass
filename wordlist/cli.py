#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from .wordlist import Wordlist

@click.command()
@click.option('-s',
        '--alt-short-wordlist',
        default=False,
        is_flag=True,
        help='Use the alternative short wordlist, with longer words that may be more memorable. Needs four dice')
def run(alt_short_wordlist):
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

    #As per EFF recomendations, roll a total of 6 times
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
