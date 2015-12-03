#!/usr/bin/python

import sys

prev_post = ''
post_id = ''
user_id = ''

for line in sys.stdin:
    line = line.strip()
    post_id, post_type, user_id = line.split("\t", 3)

    if prev_post == post_id:
        print("{0}\t{1}\t1".format(user_id, post_id))

    prev_post = post_id







