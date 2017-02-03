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

# CSV file building----
with codecs.open("twitter.txt", encoding='utf-8') as f:
    # output = open('twitter.csv', 'w')
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
        print(count, row_text, avg, sep='þ')
        count += 1
# XML file building-----
    # create the skeleton structure of the file
    count = 0
    print("<document>")
    print(" <sentences>")
    for row_text in sent:
        if len(row_text) == 0:
            continue
        tokens = word_tokenize(row_text)
        # this calculates the average word count per row
        word_count = [len(w) for w in tokens]
        sent_avg = sum(word_count) / len(word_count)
        sent_avg = str(avg)
        sent_num = str(count)
        # formatting
        row_text = row_text.replace('\n', ' ')
        sent_avg = sent_avg.replace('\n', ' ')
        sent_num = sent_num.replace('\n', ' ')
        print("  <sentence id = " + '"' + sent_num + '"' + ">")
        print("   <text>" + row_text + "</text>")
        print("   <avg>" + sent_avg + "</avg>")
        print("  </sentence>")
        count += 1
    # close out the file with the ending skeleton tags
    print(" </sentences>")
    print("</document>")
# JSON file building-----
    count = 0
    print("{")
    print(' "documents":{')
    print('  "sentences":[')
    for row_text in sent:
        if len(row_text) == 0:
            continue
        tokens = word_tokenize(row_text)
        # this calculates the average word count per row
        word_count = [len(w) for w in tokens]
        sent_avg = sum(word_count) / len(word_count)
        sent_avg = str(avg)
        sent_num = str(count)
        # formatting
        row_text = row_text.replace('\n', ' ')
        sent_avg = sent_avg.replace('\n', ' ')
        sent_num = sent_num.replace('\n', ' ')
        print("   {")
        print('    "avg":' + sent_avg)
        print('    "id":' + sent_num)
        print('    "text":' + row_text)
        # if we are at the end of the file print a comma if not, don't print a comma
        if row_text == sent[-1]:
            print("   }")
        else:
            print("   },")
        count += 1
    # finish by print out the ending tags
    print("  ]")
    print(" }")
    print("}")
