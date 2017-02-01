#!/usr/bin/python
# coding=utf-8
# ^^ because https://www.python.org/dev/peps/pep-0263/

from __future__ import division

import codecs

import json

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

# It is okay to include tokenization and symbols in the average word size count.
# Use the Thorn character (þ) to separate the fields
# Be sure to include coding=utf-8 to the first or second line

# All the output can be printed to the screen

# Note, when printing to a non-unicode terminal or using linux to write to a file
# http://stackoverflow.com/questions/4545661/unicodedecodeerror-when-redirecting-to-file

# You may need to download a corpus in nltk using the nltk.download() command.
# If you are having trouble completing feel free to post a message on the forum.

# Usage: PYTHONIOENCODING=UTF-8 python process-data.py > output.txt


with codecs.open("twitter.txt", encoding='utf-8') as f:
    # Your code here
    output = open('output.csv', 'w')
    count = 0
    f = f.read()
    sent = sent_tokenize(f)

    for row_text in sent:
        if len(row_text) == 0:
            continue
        tokens = word_tokenize(row_text)
        # this calculates the average word count per row
        word_count = [len(w) for w in tokens]
        avg = sum(word_count) / len(word_count)
        avg = str(avg)
        # print to a csv called output
        row_text = row_text.replace('\n', ' ')
        print(count, row_text, avg, sep='þ', file=output)
        count += 1
