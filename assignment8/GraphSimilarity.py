import pandas as pd

def calc_jaccard_similarity(wordset1, wordset2):
    intersection = wordset1.intersection(wordset2)
    union = wordset1.union(wordset2)
    return len(intersection) / len(union)

print("Processing Starts")
store = pd.HDFStore('store.h5')
df1 = store['df1']
df2 = store['df2']

ger_outlink = df2[df2.name == "German"].iloc[0].out_links
eu_outlink = df2[df2.name == "Europe"].iloc[0].out_links
jacc_cof_eu_germany_links = calc_jaccard_similarity(set(ger_outlink), set(eu_outlink))
print("Jaccard coeficient in Links: ", str(jacc_cof_eu_germany_links))