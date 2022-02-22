from preprocess_nitishraj37 import utils

__version__ = '0.0.2' 

def get_wordcounts(x):
	return utils.get_wordcounts(x)

def get_charcounts(x):
	return utils.get_charcounts(x)

def get_avg_wordlength(x):
	return utils.get_avg_wordlength(x)

def get_stopwords_count(x):
	return utils.get_stopwords_count(x)

def get_hashtag_counts(x):
	return utils.get_hashtag_counts(x)

def get_mentions_counts(x):
	return utils.get_mentions_counts(x)

def get_digits_count(x):
	return utils.get_digits_count(x)

def get_uppercase_counts(x):
	return utils.get_uppercase_counts(x)

def cont_exp(x):
	return utils.cont_exp(x)

def get_emails(x):
	return utils.get_emails(x)

def remove_emails(x):
	return utils.remove_emails(x)

def get_urls(x):
	return utils.get_urls(x)

def remove_urls(x):
	return utils.remove_urls(x)

def remove_rt(x):
	return utils.remove_rt(x)

def remove_special_chars(x):
	return utils.remove_special_chars(x)

def remove_html_tags(x):
	return utils.remove_html_tags(x)

def remove_accented_chars(x):
	return utils.remove_accented_chars(x)

def remove_stopwords(x):
	return utils.remove_stopwords(x)

def make_base(x):
	return utils.make_base(x)

def get_value_counts(df, col):
	return utils.get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return utils.remove_common_words(x, freq, n=20)

def remove_rarewords(x, freq, n=20):
	return utils.remove_rarewords(x, freq, n=20)

def spelling_correction(x):
	return utils.spelling_correction(x)
