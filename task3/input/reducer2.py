#!/usr/bin/python

import sys

num = 0

for line in sys.stdin:
    line = line.strip()
    count, word = line.split("\t", 2)

    if num < 1:
        print("{0}\t{1}".format(word, count))
        num += 1
