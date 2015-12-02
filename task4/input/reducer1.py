#!/usr/bin/python

import sys

prev_word = ""
word = ""
current_count = 0


for line in sys.stdin:
    line = line.strip()
    word, _ = line.split("\t", 2)

    # refresh for new word
    if prev_word != word:
        if prev_word:
            print("{0}\t{1}".format(prev_word, current_count))
            current_count = 0

    prev_word = word
    current_count += 1

print("{0}\t{1}".format(word, current_count))





