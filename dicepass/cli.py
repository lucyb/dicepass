#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from . import dicepass

@click.command()
@click.option('-a',
        '--alt-short-wordlist',
        default=False,
        is_flag=True,
        help='Use the alternative short wordlist, with longer words that may be more memorable. Needs four dice')
@click.option('-s',
        '--short-wordlist',
        default=False,
        is_flag=True,
        help='Use the short wordlist. This is assumed to be true if four dice are entered and the alternative wordlist hasn\'t been selected')
@click.option('-r',
        '--random',
        default=False,
        is_flag=True,
        help='Rely on machine generated random numbers to generate passphrases.')
def run(alt_short_wordlist, short_wordlist, random):
    if (random):
        dicepass.random_generator(alt_short_wordlist, short_wordlist)
    else:
        dicepass.walkthrough(alt_short_wordlist)
