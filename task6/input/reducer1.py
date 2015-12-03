#!/usr/bin/python

import sys

num = 0

for line in sys.stdin:
    line = line.strip()
    count, post_id = line.split("\t", 2)

    if num < 10:
        print("{0}\t{1}".format(count, post_id))
        num += 1







