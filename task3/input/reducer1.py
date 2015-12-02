#!/usr/bin/python

import sys

prev_word = ""
word = ""
current_count = 0

max_count = 0
max_word = ''


for line in sys.stdin:
    line = line.strip()
    word, _ = line.split("\t", 2)

    # refresh for new word
    if prev_word != word:
        if current_count > max_count:
            max_word = prev_word
            max_count = current_count
        current_count = 0

    prev_word = word
    current_count += 1

# check last word
if prev_word == word:
    if current_count > max_count:
        max_word = word
        max_count = current_count

print("{0}\t{1}".format(max_word, max_count))





