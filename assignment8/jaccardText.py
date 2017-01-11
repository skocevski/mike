from pathlib import Path
import pandas as pd
import re
import math
from collections import Counter
import numpy as np

def splitText(text):
    text = re.sub('[^A-Za-z0-9\s]+', '', text.lower())
    return re.split(r'\s+', text)

def makeWordSet(text):
    words = splitText(text)
    listofWords = set()
    for word in words:
        listofWords.add(word)
    return listofWords

def gen_word_set(data_frame):
    results = []
    for _, row in data_frame.iterrows():
        results.append(makeWordSet(row.text))
    data_frame['word_set'] = results

def calc_jaccard_similarity(wordset1, wordset2):
    """Calculates jaccard similarity from given sets"""
    intersection = wordset1.intersection(wordset2)
    union = wordset1.union(wordset2)
    return len(intersection) / len(union)

print("Processing Starts")
store = pd.HDFStore('store.h5')
df1 = store['df1']
df2 = store['df2']
gen_word_set(df1)

ger_wordset = df1[df1.name == "German"].iloc[0].word_set
eu_wordset = df1[df1.name == "Europe"].iloc[0].word_set
jacc_cof_eu_germany = calc_jaccard_similarity(eu_wordset, ger_wordset)
print("Jaccard similarity on sets", str(jacc_cof_eu_germany))