#!/usr/bin/python

import sys

word = ''
prev_word = ''
doc_count = 1

file_name = ''
prev_doc = ''
word_count = 0

for line in sys.stdin:
    line = line.strip()
    word, file_name, count = line.split("\t", 2)

    # refresh for new word
    if prev_word != word:
        # ignore the first line
        if prev_word:
            # write the doc count and the previous doc
            sys.stdout.write("({0},{1})".format(prev_doc, word_count))
            sys.stdout.write("}:" + str(doc_count))
            print("")
            doc_count = 1
            word_count = 0
            prev_doc = file_name

            # write the new word
            sys.stdout.write(str(word) + ":{")
        else:
            # print the name for line 1
            sys.stdout.write(str(word) + ":{")
    else:
        # refresh for new doc
        if prev_doc != file_name:
            sys.stdout.write("({0},{1}),".format(prev_doc, word_count))
            doc_count += 1
            word_count = 0

    # update previous variables
    prev_word = word
    prev_doc = file_name
    word_count += 1

if file_name == prev_doc:
    sys.stdout.write("({0},{1})".format(prev_doc, word_count))

if prev_word == word:
    sys.stdout.write("}:" + str(doc_count))
    print("")






