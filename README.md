# EFF Wordlist Reference #

Arnold G. Reinhold created the Diceware word list some years ago to provide a system for generating secure passphrases. It has since become widely used within the infosec community. This original list has recently been improved upon by the EFF, who have generated newer lists that overcome some of Diceware's shortcomings. However, they are long and inconvenient to carry around. So to save on printing, this python program will reference those lists and print out the word for a given dice result.

To use, just type *wordlist* and provide the dice rolls..

When a five dice are used *wordlist* will use the long wordlist provided by the EFF. This is the most secure option.

If only four dice are supplied, *wordlist* will use the short wordlist. This may result in a passphrase that's easier to type and should be secure enough for most situations.

If *wordlist* is run with the -t flag then it will use the alternative short wordlist, which contains longer words that may be more memorable.

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

Usage: wordlist [OPTIONS]

Options:
        -t, --alt-short-wordlist  Use the alternative short wordlist, with longer
                                  words that may be more memorable. Needs four dice
        --help                    Show this message and exit.
```