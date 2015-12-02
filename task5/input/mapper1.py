#!/usr/bin/python
import sys
import time
import datetime

# format of request
# msfcsma3.msfc.nasa.gov - - [01/Aug/1995:13:24:29 -0400] "GET /shuttle/missions/missions.html HTTP/1.0" 200 8677


for line in sys.stdin:
    line = line.strip()
    # extract and separate the request
    host = line.split()[0]
    datetime_raw = line.partition('[')[-1].partition(']')[0]
    timestamp = time.mktime(datetime.datetime.strptime(datetime_raw, "%d/%b/%Y:%H:%M:%S -0400").timetuple())
    print("{0}\t{1}\t{2}".format(host, timestamp, 1))






