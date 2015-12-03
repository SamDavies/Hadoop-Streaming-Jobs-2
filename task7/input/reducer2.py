#!/usr/bin/python

import sys

num = 0

for line in sys.stdin:
    line = line.strip()
    count, user_id, posts = line.split("\t", 3)

    if num < 1:
        print(line)
        num += 1







