import re


def only_letters(string):
    return re.fullmatch('[a-z]*', string)
