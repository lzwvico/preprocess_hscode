import re
import os
import sys

import pandas as pd
import numpy as np
import langid
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from spacy_langdetect import LanguageDetector
from nltk.classify.textcat import TextCat
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


add_stop = ['', ' ', 'say', 's', 'u', 'ap', 'afp', '...', 'n', '\\',
            'baik', 'dan', 'baru', ' x ', ' ii', ' mm',
            ' kg', ' kgm','ml','red',' l'
           'pcs', 'promotional','promotion','free of charge','ml','foc']

stop_words = ENGLISH_STOP_WORDS.union(add_stop) 


def _get_wordcounts(x):
    length = len(str(x).split())
    return length
    
def _get_charcounts(x):
    s = x.split()
    x = ''.join(s)
    return len(x)
    
def _get_stopwordscounts(x):
	l = len([t for t in x.split() if t in stopwords])
	return l
    
def _remove_specialchars(x):
	x = re.sub(r'[^\w ]+', "", x)
	x = ' '.join(x.split())
	return x
     
def _remove_accentedchars(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x
     
def _lowcase_convert(x):
	lowercase = str(x).lower()
	return lowercase
       
def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t not in stopwords])


## Pahami karakteristik uraian barang pada HS terkait sebelum memanggil fungsi ini

def _remove_common_words(x, freq, n=20): # set di 20, adjust sesuai kebutuhan
	fn = freq[:n]
	x = ' '.join([t for t in x.split() if t not in fn])
	return x

def _remove_rarewords(x, freq, n=20): # set di 20, adjust sesuai kebutuhan
	fn = freq.tail(n)
	x = ' '.join([t for t in x.split() if t not in fn])
	return x	
    
##---------------------------------------------------------------------##


