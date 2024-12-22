import nltk
import string
from nltk.corpus import stopwords  # Import stopwords
"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

"""
def tokenize_text(text, remove_stopwords=True):
    
    Tokenize text using the nltk library
    
    
    tokens = []
    stop_words = set(stopwords.words('english')) if remove_stopwords else set()
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            word = word.lower()
            # filters here
            if word not in stop_words and word not in string.punctuation:
                tokens.append(word)
    return tokens
"""

def tokenize_text(text, remove_stopwords=True):
    """
    Tokenize text using the nltk library and remove unwanted tokens
    """
    
    tokens = []
    # Define stopwords
    stop_words = set(stopwords.words('english')) if remove_stopwords else set()
    
    # Define unwanted tokens to filter
    unwanted_tokens = {"'s", "n't", "'m", "'re", "'ve", "'d", "'ll"}
    
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            word = word.lower()
            # Remove stopwords, punctuation, and unwanted tokens
            if word not in stop_words and word not in string.punctuation and word not in unwanted_tokens:
                tokens.append(word)
    return tokens
