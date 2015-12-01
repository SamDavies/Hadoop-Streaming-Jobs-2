#!/usr/bin/python

import sys

word = ''
score = ''
doc = ''

prev_word = ''

for line in sys.stdin:
    line = line.strip()
    word, score, doc = line.split("\t", 2)

    # refresh for new word
    if prev_word != word:
        # ignore the first line
        if prev_word:
            print("{0}, {1} = {2}".format(prev_word, doc, score))
        prev_word = word


if prev_word == word:
    print("{0}, {1} = {2}".format(word, doc, score))






