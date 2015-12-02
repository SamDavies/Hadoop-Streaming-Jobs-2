#!/usr/bin/python

import sys
import datetime

first_timestamp = ''
timestamp_raw = ''
request_count = 0

prev_host = ""
prev_timestamp_raw = ""
host = ""


def print_host_time_diff(host_name, num_requests, last, first):
    """
    Calculate the time diff and print to stdout
    :param host_name: the name of the host
    :param num_requests: the number of requests from this host
    :param last: the last timestamp from this host
    :param first: the last timestamp from this host
    :return: nothing
    """
    last = datetime.datetime.fromtimestamp(float(last))
    if num_requests > 1:
        # calclate the time difference between the first and last request from this host
        first = datetime.datetime.fromtimestamp(float(first))
        time_diff = last - first
        print("{0}\t{1}".format(host_name, time_diff))
    else:
        # for 1 request just print the timestamp
        print("{0}\t{1}".format(host_name, last))

for line in sys.stdin:
    line = line.strip()
    host, timestamp_raw, _ = line.split("\t", 3)

    # refresh for new host
    if prev_host != host:
        if prev_host:
            # check if more than 1 request was made
            print_host_time_diff(prev_host, request_count, prev_timestamp_raw, first_timestamp)

        first_timestamp = timestamp_raw
        request_count = 0

    prev_host = host
    prev_timestamp_raw = timestamp_raw
    request_count += 1

print_host_time_diff(host, request_count, timestamp_raw, first_timestamp)







