from preprocess_hscode import utils

__version__ = '0.0.1'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_stopwordscounts(x):
	return utils._get_stopwords_counts(x)
    
def remove_specialchars(x):
	return utils._remove_special_chars(x)
    
def remove_accentedchars(x):
	return utils._remove_accented_chars(x)
    
def lowcase_convert(x):
	return utils._lowcase_convert(x)   
    
def remove_stopwords(x):
	return utils.remove_stopwords(x)

def remove_common_words(x, freq, n=20):
	return utils._remove_common_words(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return utils._remove_rarewords(x, freq, n)

