#!/usr/bin/python

import sys

num = 0

for line in sys.stdin:
    line = line.strip()
    count, user_id, posts = line.split("\t", 3)

    if num < 1:
        print("{0}\t->\t{1}\t{2}".format(user_id, count, posts))
        num += 1







