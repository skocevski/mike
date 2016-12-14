import string
import random
import sys
words = lines = 0
zipf_prob = {' ': 0.17840450037213465, '1': 0.004478392057619917, '0': 0.003671824660673643, '3': 0.0011831834225755678, '2': 0.0026051307175779174, '5': 0.0011916662329062454, '4': 0.0011108979455528355, '7': 0.001079651630435706, '6': 0.0010859164582487295, '9': 0.0026071152282516083, '8': 0.0012921888323905763, '_': 2.3580656240324293e-05, 'a': 0.07264712490903191, 'c': 0.02563767289222365, 'b': 0.013368688579962115, 'e': 0.09688273452496411, 'd': 0.029857183586861923, 'g': 0.015076820473031856, 'f': 0.017232219565845877, 'i': 0.06007894642873102, 'h': 0.03934894249122837, 'k': 0.006067466280926215, 'j': 0.0018537015877810488, 'm': 0.022165129421030945, 'l': 0.03389465109649857, 'o': 0.05792847618595622, 'n': 0.058519445305660105, 'q': 0.0006185966212395744, 'p': 0.016245321110753712, 's': 0.055506530071283755, 'r': 0.05221605572640867, 'u': 0.020582942617121572, 't': 0.06805204881206219, 'w': 0.013964469813783246, 'v': 0.007927199224676324, 'y': 0.013084644140464391, 'x': 0.0014600810295164054, 'z': 0.001048859288348506}

uni_prob = {' ': 0.1875, 'a': 0.03125, 'c': 0.03125, 'b': 0.03125, 'e': 0.03125, 'd': 0.03125, 'g': 0.03125, 'f': 0.03125, 'i': 0.03125, 'h': 0.03125, 'k': 0.03125, 'j': 0.03125, 'm': 0.03125, 'l': 0.03125, 'o': 0.03125, 'n': 0.03125, 'q': 0.03125, 'p': 0.03125, 's': 0.03125, 'r': 0.03125, 'u': 0.03125, 't': 0.03125, 'w': 0.03125, 'v': 0.03125, 'y': 0.03125, 'x': 0.03125, 'z': 0.03125}

def makeTotal(l):
    i = 0
    n = []
    for k, v in l.iteritems():
        i += v
        n.append([i, k, v])
    return n

def getChar(l, t):
    i = 0
    n = []
    for i in range(0, len(l)):
         if(l[i][0] == t):
           return l[i][1]

def genText(l, fileName):
    ii = 0
    s = ""
    #for i in range(0, (chars+spaces)):
    for i in range(0, 100000):#for testing...
        v = min([row[0] for row in l], key=lambda x:abs(x-random.random()))
        s += getChar(l, v)
        ii+=1
    if ii >1000:
        sys.stdout.write('  _'+str(i)+'_   ')
        ii=0
        with open(fileName, "w") as file:
            file.write(s)
with open("articles.txt",'r', encoding="utf-8") as in_file:
    for line in in_file:
        lines += 1
        words += len(line.split())
        spaces= (words-lines)

print ("Total number of lines are :", lines)
print ("Total number of words are :", words)
print ("Total number of spaces are :", spaces)
filee = open("articles.txt", "r", encoding="utf-8")
data=filee.read()
words = data.split()
chars = 0
for i in words:
   chars += len(i)
print ("Total number of characters are :", chars)
print ("n as mentioned, is sum of characters and spaces :", chars+spaces)
tot_uni_prob = makeTotal(uni_prob)
tot_zipf_prob = makeTotal(zipf_prob)
genText(tot_uni_prob, "uni.txt")
genText(tot_zipf_prob, "zipf.txt")