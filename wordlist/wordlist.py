#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Wordlist(object):
    wordlists = {
        "long"   : "eff_large_wordlist.txt",
        "short"  : "eff_short_wordlist_1.txt",
        "short2" : "eff_short_wordlist_2_0.txt"
    }

    def __init__(self, num_dice, alt_short_wordlist):
        #Default to using large wordlist, unless only 4 dice are used
        #or the alternative short wordlist is specified
        file_name = Wordlist.wordlists["long"]
        if num_dice == 4:
            file_name = Wordlist.wordlists["short"]
        if alt_short_wordlist:
            file_name = Wordlist.wordlists["short2"]

        #Read in the appropriate wordlist
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
