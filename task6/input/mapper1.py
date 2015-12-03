#!/usr/bin/python
import re
import sys

# format of request
# msfcsma3.msfc.nasa.gov - - [01/Aug/1995:13:24:29 -0400] "GET /shuttle/missions/missions.html HTTP/1.0" 200 8677


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

    # do the query
    if data.get("PostTypeId") == '1':
        post_id = data.get("Id")
        view_count = data.get("ViewCount")
        print("{0}\t{1}".format(view_count, post_id))
