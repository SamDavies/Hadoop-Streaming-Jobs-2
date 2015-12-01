#!/usr/bin/python
import sys

import math

search_doc = 'd1.txt'
total_docs = 17.0

# First load the dictionary.
terms = set()
for line in file('terms.txt'):
    terms.add(line.strip())


def get_search_doc_word_count(raw, doc_count):
    """
    Extract the word count for the serach document
    :param raw: the raw string to parse
    :param doc_count: the number of documents which the word occurs in
    :return: the count of the word occurrences in the search document, 0 if not fount
    """
    for i in range(int(doc_count)):
        doc, word_count = raw.partition('(')[-1].partition(')')[0].split(',', 1)
        if doc == search_doc:
            return word_count
    return 0


def calculate_tf_idf(term, freq, docs_occur):
    """
    Calculates the term frequency-inverse document frequency
    :param term: the word
    :param freq: the number of occurrences of the term inside the search document
    :param docs_occur: the number of documents where the term appears
    :return: the term frequency-inverse document frequency
    """
    return float(freq) * math.log(total_docs/(1.0 + float(docs_occur)), 10)

for line in sys.stdin:
    line = line.strip()
    word, doc_count, word_counts_raw = line.split(":", 2)

    if word in terms:
        search_doc_word_count = get_search_doc_word_count(word_counts_raw, doc_count)
        score = calculate_tf_idf(word, search_doc_word_count, doc_count)
        print("{0}\t{1}\t{2}".format(word, score, search_doc))
        terms.remove(word)


# print all the missing terms
for term in terms:
    print("{0}\t{1}\t{2}".format(term, 0.0, search_doc))





