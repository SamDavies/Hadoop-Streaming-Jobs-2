#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    word, word_counts, doc_count = line.split(":", 2)
    print("{0}:{1}:{2}".format(word, doc_count, word_counts))


