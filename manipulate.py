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

# CSV file building
with codecs.open("twitter.txt", encoding='utf-8') as f:
    output = open('twitter.csv', 'w')
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
# XML file building
with open('twitter.csv', encoding='utf-8') as g:
    # create a new output file for XML
    output = open('twitter.xml', 'w')
    # create the skeleton structure of the file
    print("<document>", file=output)
    print(" <sentences>", file=output)
    for row_text in g:
        # splitting the csv file
        # print(row_text)
        sent_num, sent_text, sent_avg = row_text.split("þ")
        sent_avg = str(sent_avg)
        sent_avg = sent_avg.replace('\n', '')
        print("  <sentence id = " + '"' + sent_num + '"' + ">", file=output)
        print("   <text>" + sent_text + "</text>", file=output)
        print("   <avg>" + sent_avg + "</avg>", file=output)
        print("  </sentence>", file=output)
    # close out the file with the ending skeleton tags
    print(" </sentences>", file=output)
    print("</document>", file=output)
