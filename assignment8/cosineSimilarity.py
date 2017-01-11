from pathlib import Path
import pandas as pd
import re
import math
from collections import Counter
import numpy as np


def CountFreq(data_frame):
    """ Calculates the frequency of each term in each article"""
    results = []
    for _, row in data_frame.iterrows():
        results.append(CalculateTermFreq(row.text))
    data_frame['term_freq'] = results

def docFrequency(input_terms, documents):
    """ Calculate the document frequency of each term in given documents"""
    results = dict()
    for term in input_terms:
        print("Processing ", term)
        result = cal_doc_freq_of_term(term, documents)
        results[term] = result[term]
    return results

def calculate_cosine_similarity(tfIdfDict1, tfIdfDict2):
    """ Calculates cosines similarity"""
    scalar_product_article1_article2 = 0
    for each_term_article1 in tfIdfDict1:
        if each_term_article1 in tfIdfDict2.keys():
            scalar_product_article1_article2 = scalar_product_article1_article2 + (tfIdfDict1[each_term_article1] * tfIdfDict2[each_term_article1])

    euc_dist_tfIdfDict1 = np.sum(np.square(list(tfIdfDict1.values())))
    euc_dist_tfIdfDict2 = np.sum(np.square(list(tfIdfDict2.values())))

    cosineSimilarity = scalar_product_article1_article2 / (euc_dist_tfIdfDict1 * euc_dist_tfIdfDict2)
    return cosineSimilarity

def cal_tfidf_each_term(data_frame, document_term_freq):
    """ Calculates the tfidf of each term"""
    results = []
    doc_length = len(data_frame.term_freq)
    for _, row in data_frame.iterrows():
        term_set = row.term_freq
        res = dict()
        for term in term_set:
            res[term] = tfidf(term_set[term], doc_length, document_term_freq[term])
        results.append(res)
    data_frame['tf_idf'] = results

def CalculateTermFreq(text_document):
    """ Calculate frequency of each word in given document"""
    words = SplitText(text_document)
    gen_freq = dict(Counter(words))
    return gen_freq

def SplitText(text):
    """ Split given text with spaces """
    text = re.sub('[^A-Za-z0-9\s]+', '', text.lower())
    return re.split(r'\s+', text)

def tfidf(term_freq, total_doc, match_doc):
    """ Calculates term frequency inverse document frequency"""
    return term_freq * math.log((total_doc/match_doc))

print("Processing Starts")

store = pd.HDFStore('store.h5')
df1 = store['df1']
df2 = store['df2']

# calculating term frequency
CountFreq(df1)
term_document_freq = None

doc_feq = Path('./doc_freq.txt')

if doc_feq.is_file():
      with open('doc_freq.txt', 'r+') as f:
          term_document_freq = eval(f.read())
else:
    term_document_freq = docFrequency(all_terms, all_docs)
    with open('doc_freq.txt', 'w+') as f:
        f.write(str(term_document_freq))


cal_tfidf_each_term(df1, term_document_freq)
ger_tf_idf = df1[df1.name == "German"].iloc[0].tf_idf
eu_tf_idf = df1[df1.name == "Europe"].iloc[0].tf_idf

print("Jaccard", calculate_cosine_similarity(ger_tf_idf, eu_tf_idf))
