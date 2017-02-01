import math

f1=open("onlyhash.data", "r", encoding="utf -8")
m = f1.read()
splittedContent = m.split('\n')

print(len(splittedContent))

i = 0
counter = 0
users = []
NuTweets = []
for i in range(len(splittedContent) - 1):
    j = 0
    rowSpletted = splittedContent[i].split()
    userN = rowSpletted[0]
    if (userN in users):
        continue
    else:
        users.append(userN)
        counter = 0
        while (j < 10000):
            rwSpl = splittedContent[j].split()
            usrN = rwSpl[0]
            if(userN == usrN):
                counter = counter + 1
            j = j + 1
        NuTweets.append(counter)
    print(str(i))

userEntropy = []
for i in NuTweets:
    userEntropy.append((1/NuTweets[i]) +  math.log(1/NuTweets[i], 10))

memes = []
dates = []
for i in range(len(splittedContent) - 1):
    rowSpletted = splittedContent[i].split()
    meme = rowSpletted[2]
    date = rowSpletted[1]
    memes.append(meme)
    dates.append(date)

date_meme_list = []
if not date in dates:
    dates.append(date)
    date_meme_list.append({})
else:
    for one in memes:
        ind = dates.index(date)
    if one in date_meme_list[ind]:
        date_meme_list[ind][one] += 1
    else:
        date_meme_list[ind][one] = 1

sys_entro = []
for index in range(len(dates)):
    entro = 0
    n = sum(date_meme_list[index][one] for one in date_meme_list[index])
    for meme in date_meme_list[index]:
        fu = date_meme_list[index][meme] / n
        entro -= fu * (math.log10(fu))
    sys_entro.append(entro)


from matplotlib import pyplot as plt
import numpy as np

plt.plot(userEntropy, color="red")
plt.plot(sys_entro, color="blue")
x = np.arange(0, len(dates), 1)
# print (x,len(order_sys_entropy))
plt.xlim(1, len(dates) + 1)
plt.ylim(0, sys_entro[len(dates) - 1])
# set the caption
plt.title('Daily system entropy', fontsize=10, fontweight='bold')
# the label of x-axis
plt.xlabel('rank')
# the label of y-axis
plt.ylabel('entropy')
plt.show()