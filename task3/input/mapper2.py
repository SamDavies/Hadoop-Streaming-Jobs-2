#!/usr/bin/python
import sys

# format of request
# msfcsma3.msfc.nasa.gov - - [01/Aug/1995:13:24:29 -0400] "GET /shuttle/missions/missions.html HTTP/1.0" 200 8677


for line in sys.stdin:
    line = line.strip()
    # extract and separate the request
    host, count = line.split('\t', 2)
    print("{0}\t{1}".format(count, host))




