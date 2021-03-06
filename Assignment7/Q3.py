import random
import numpy as np
import matplotlib.pyplot as plt
import collections
def rollDiceGetSum():
    return random.randint(1, 6) + random.randint(1, 6)
def calculateCDF(result):
    frequencyNum = collections.Counter(result).most_common()
    total = sum([frequency for (key, frequency) in frequencyNum])
    probabilityForEachNumDict = {}
    for (key, frequency) in frequencyNum:
        probabilityForEachNumDict[key] = frequency / \
                                          total
    arrayForCDFCalc = list(probabilityForEachNumDict.values())
    a = np.array(arrayForCDFCalc)
    cdfEvalDict = np.cumsum(a)
    return (list(probabilityForEachNumDict.keys()), cdfEvalDict)
def drawHistogram(sumResult):
    plt.hist(sumResult, bins=[2,3,4,5,6,7,8,9,10,11,12])
    plt.title('Histogram with frequencies of dice sum outcomes from the simulation', y=1.06)
    plt.ylabel('Frequencies')
    plt.xlabel('Different Sum Results')
    plt.xticks(np.arange(2, 13, 1))
    plt.grid('on')
    plt.show()
def drawSingleCDF(sumResult, median, probLessNnine):
    (xval, cdfval) = calculateCDF(sumResult)
    plt.title("CDF PLOT for 100 times rolling two dice(sum of two dice)")
    plt.xlabel("Different Sum Results")
    plt.ylabel("Cumulative frequency in percentage")
    plt.grid('on')
    plt.xticks(np.arange(2, 13, 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.plot(xval, cdfval, drawstyle='steps-post', label='CDF')
    plt.plot((2, 13), (.5, .5))
    plt.plot((median, median), (0, .5))
    plt.annotate('Median: %d' % median, (median, .5), xytext=(0.7, 0.7), arrowprops=dict(arrowstyle='->'))
    plt.plot((2, 13), (probLessNnine, probLessNnine))
    plt.annotate('Probability (<=9): %s' % probLessNnine, (9, probLessNnine), xytext=(1, 0.9),
                 arrowprops=dict(arrowstyle='->'))
    plt.legend(loc=0)
    plt.show()
def drawDoubleCDF(result1, result2, n):
    (xval1, cdfval1) = calculateCDF(result1)
    (xval2, cdfval2) = calculateCDF(result2)
    maxDist = getMaxDistance(cdfval1, cdfval2)
    print(" The maximum pointwise distance between two CDFs for n= " + str(n)+ ", is =" + str(maxDist))
    plt.title("CDF PLOT for " + str(n) + " times rolling two dice(sum of two dice)")
    plt.xlabel("Different Sum Results of rolling of two diece")
    plt.ylabel("Cumulative frequency in percentage")
    plt.xticks(np.arange(2, 13, 1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.plot(xval1, cdfval1, drawstyle='steps-post', label='CDF for first time')
    plt.plot(xval2, cdfval2, drawstyle='steps-post', label='CDF for second time')
    plt.grid('on')
    plt.legend(loc=0)
    plt.show()
def rollDice(n):
    sumResult = []
    for _ in range(n):
        result = rollDiceGetSum()
        sumResult.append(result)
    sumResult = np.sort(sumResult)
    return sumResult
def getMedian(sumResult):
    a = np.array(sumResult)
    print("Median val: ", np.median(a))
    return np.median(a)
def getProbByVal(arr, val):
    gen = [x for x in arr if x<= val]
    return (len(gen)/len(arr))
def getMaxDistance(result1, result2):
    diffResult = [abs(x - y) for x, y in zip(result1, result2)]
    return max(diffResult)
def main():
    sumResult = rollDice(100)
    drawHistogram(sumResult)
    median = getMedian(sumResult)
    val = getProbByVal(sumResult, 9)
    drawSingleCDF(sumResult, median, val)
    sumResult1 = rollDice(100)
    drawDoubleCDF(sumResult, sumResult1, 100)
    result1 = rollDice(1000)
    result2 = rollDice(1000)
    drawDoubleCDF(result1, result2, 1000)
if __name__ == '__main__':
    main()
