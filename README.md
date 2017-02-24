# EFF Wordlist Reference #

Arnold G. Reinhold created the Diceware word list some years ago to provide a system for generating secure passphrases. It has since become widely used within the infosec community. This original list has recently been improved upon by the EFF, who have generated newer lists that overcome some of Diceware's shortcomings. However, they are long and inconvenient to carry around. So to save on printing, this python program will reference those lists and print out the word for a given dice result.

To use, just type *dicepass* and provide the dice rolls..

When a five dice are used *dicepass* will use the long dicepass provided by the EFF. This is the most secure option.

If only four dice are supplied, *dicepass* will use the short dicepass. This may result in a passphrase that's easier to type and should be secure enough for most situations.

If *dicepass* is run with the -t flag then it will use the alternative short dicepass, which contains longer words that may be more memorable.

For more information see https://www.eff.org/dice.


## Installation ##

Install using setup tools by doing:
```
#!bash

python setup.py install
```


## Usage ##

```
#!bash

Usage: dicepass [OPTIONS]

Options:
        -a, --alt-short-dicepass  Use the alternative short dicepass, with longer
                                  words that may be more memorable. Needs four dice.
        -s, --short-dicepass      Use the short dicepass. This is assumed to be true
                                  if four dice are entered and the alternative
                                  dicepass hasn't been selected.
        -r, --random              Rely on machine generated random numbers to
                                  generate passphrases.
        --help                    Show this message and exit.
```
