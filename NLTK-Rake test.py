# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import gensim


import pdfminer3
txt = "C:/RandD/Ex1/test-EVD-SEARO.txt"

openfile = open(txt, "r")

lines = openfile.readlines()

import rake_nltk
from rake_nltk import Rake

r = Rake()# Uses stopwords for english from NLTK, and all puntuation characters.

r.extract_keywords_from_sentences(lines)

phraselist = r.get_ranked_phrases_with_scores() # To get keyword phrases ranked highest to lowest.

for i in phraselist[:5]:
    print("Line: ", i[1], " score: ", i[0] )