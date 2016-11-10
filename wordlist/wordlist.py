#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Wordlist(object):
    large_wordlist = "eff_large_wordlist.txt"
    short_wordlist = "eff_short_wordlist_1.txt"
    short_wordlist_long = "eff_short_wordlist_2_0.txt"

    def __init__(self, num_dice):
        #Default to using large wordlist
        file_name = Wordlist.large_wordlist
        if num_dice == 4:
            file_name = Wordlist.short_wordlist
        self.wordlist_file = os.path.join(os.path.dirname(__file__), file_name)
        self.wordlist = self.read_wordlist(self.wordlist_file)

    def select(self, die):
        return self.wordlist[die]

    def read_wordlist(self, filename):
        '''Read in the wordlist
        '''
        w = {}
        with open(filename) as fd:
            w = dict(line.strip().split(None, 1) for line in fd)
        return w
