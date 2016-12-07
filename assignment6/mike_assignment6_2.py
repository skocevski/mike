import numpy as np

f1=open("SEWcontent.txt", "r", encoding="utf-8")
m = f1.read()
splittedContent = m.split(' ')

print("Total number of words in all articles in Simple English Wikipedia is: \t " + str(len(splittedContent)))
AE = open("us wordss.txt", "r", encoding="utf-8")
aew = AE.read()
splittedAE = aew.split('\n')
print("Total number of American English words: \t " + str(len(splittedAE)))

BE = open("be words.txt", "r", encoding="utf-8")
bew = BE.read()
splittedBE = bew.split('\n')
print("Total number of British English words: \t " + str(len(splittedBE)))

def Countwords(splA):
    lst=list()
    for j in range(0, len(splA)):
        if(j%400==0):
            print("Word  number:" + str(j) + " / " + ""  + str(len(splA)) + "\t " + splA[j])
        x = (str(m)).count(splA[j])
        lst.append(x)
    return lst


resAE = Countwords(splittedAE)
resBE = Countwords(splittedBE)

print("American words found in SEW:" + str(resAE))
print("British words found in SEW:" + str(resBE))

from matplotlib import pyplot as plt

print("Mean of American English words\t ", np.mean(resAE))
print("Mean of British English words\t " , np.mean(resBE))

print("Medien of British English words\t ", np.median(resAE))
print("Medien of British English words\t ", np.median(resBE))

plt.hist(resAE, bins = np.arange(0, 1300, 5), normed=True, color='yellow', label="American English words")
plt.hist(resBE, bins = np.arange(0, 1300, 5), normed=True, color='gray', label="British English words")
plt.title("Compairing of the usage of words from American and British English")
plt.xlabel("Number of words")
plt.ylabel("Frequency")
plt.legend( shadow=True, fancybox=True)
plt.show()

