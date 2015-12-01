#!/usr/bin/python
import os
import sys

for line in sys.stdin:
    file_name = os.path.basename(os.environ["mapreduce_map_input_file"])
    file_name = file_name.strip()

    line = line.strip()
    words = line.split()

    for word in words:
        print("{0}\t{1}\t{2}".format(word.replace(":", ""), file_name, 1))
