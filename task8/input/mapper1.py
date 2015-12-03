#!/usr/bin/python
import re
import sys

# post_id   1   1
# post_id   2   user_id

# -> user_id    post_id

# user_id   ->  235 ->  posts

for line in sys.stdin:
    line = line.strip()
    # extract and separate the request
    line = line[4:][:-2].strip()
    # get the raw data as a list of strings
    data_raw = re.findall(r'\S+"\S+"', line)
    # get the attribute and values from the raw string

    data = dict()
    for pair in data_raw:
        pair = pair.split("=")
        if len(pair) > 1:
            value = pair[1][1:][:-1]
            data[pair[0]] = value

    # get the questions
    if data.get("PostTypeId") == '1':
        post_id = data.get("AcceptedAnswerId")
        if post_id:
            print("{0}\t1\t1".format(post_id))

    # get the answers
    if data.get("PostTypeId") == '2':
        post_id = data.get("Id")
        user_id = data.get("OwnerUserId")
        if post_id:
            print("{0}\t2\t{1}".format(post_id, user_id))
