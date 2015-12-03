#!/usr/bin/python

import sys

prev_user = ''
prev_post = ''
post_count = 0
current_post_list = ''

user_id = ''
post_id = ''

for line in sys.stdin:
    line = line.strip()
    user_id, post_id, _ = line.split("\t", 3)

    if prev_user != user_id:
        if prev_user:
            print("{0}\t{1}\t{2}".format(post_count, prev_user, current_post_list))
        post_count = 0
        prev_post = ''
        current_post_list = ''

    if prev_post != post_id:
        # append the previous post id to the list for this user
        if post_count != 0:
            current_post_list += ', '
        current_post_list += post_id
        post_count += 1

    prev_user = user_id
    prev_post = post_id


if prev_user == user_id:
    print("{0}\t{1}\t{2}".format(post_count, user_id, current_post_list))







