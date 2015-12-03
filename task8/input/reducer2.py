#!/usr/bin/python

import sys

prev_user = ''
prev_post = ''
post_count = 0
current_post_list = ''

user_id = ''
post_id = ''

max_post_count = 0
max_user = ''
max_post_list = ''

for line in sys.stdin:
    line = line.strip()
    user_id, post_id, _ = line.split("\t", 3)

    if prev_user != user_id:
        if prev_user:
            if post_count > max_post_count:
                max_post_count = post_count
                max_user = prev_user
                max_post_list = current_post_list
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
    if post_count > max_post_count:
        max_post_count = post_count
        max_user = user_id
        max_post_list = current_post_list

print("{0}\t{1}\t{2}".format(max_post_count, max_user, max_post_list))