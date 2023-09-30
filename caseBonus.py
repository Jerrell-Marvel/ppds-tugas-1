# =================================
# Nikolas Giovanni (6182201009)
# Christian Hadinata (6182201020)
# Jerrell Marvel (6182201035)
# =================================

import glob
import math

folderPathList = glob.glob("C:\\Kuliah\\kuliah-sem-3\\ppds\\tugas\\bbc\\*")

wordFreqList = []

for currFolderPath in folderPathList:
    filePathList = glob.glob(currFolderPath + "\\*.txt")

    wordFreqDict = {}

    for currFilePath in filePathList:
        fh = open(currFilePath, "r")

        currLine = fh.readline()

        while (len(currLine) != 0):
            wordList = currLine.lower().split()

            for currWord in wordList:
                hasDigit = False

                for currChar in currWord:
                    if currChar.isnumeric():
                        hasDigit = True

                if hasDigit == False:
                    wordFreq = wordFreqDict.get(currWord)
                    if wordFreq == None:
                        wordFreqDict[currWord] = 1
                    else:
                        wordFreqDict[currWord] = wordFreq + 1
            currLine = fh.readline()

        fh.close()

    wordFreqList.append(wordFreqDict)

##############################################################################
# OUTLIER
wordMarkerList = []
wordFreqAvgDict = {}
wordStandardDevDict = {}

ZSCORELIMIT = 1.9

for currWordFreq in wordFreqList:
    subWordMarkerList = []

    for currKey in currWordFreq.keys():
        wordAverage = wordFreqAvgDict.get(currKey)
        standardDev = wordStandardDevDict.get(currKey)

        if wordAverage == None:
            standardDev = 0
            totalFreq = 0
            for wordFreq in wordFreqList:
                tempWordFreq = wordFreq.get(currKey)
                if (tempWordFreq != None):
                    totalFreq += tempWordFreq
            wordAverage = totalFreq / len(wordFreqList)
            wordFreqAvgDict[currKey] = wordAverage

            for wordFreq in wordFreqList:
                tempWordFreq = wordFreq.get(currKey)

                if tempWordFreq is None:
                    tempWordFreq = 0

                standardDev += math.pow(tempWordFreq - wordAverage, 2)

            standardDev = math.sqrt(standardDev / len(wordFreqList))
            wordStandardDevDict[currKey] = standardDev

        if standardDev != 0:
            zScore = (currWordFreq.get(currKey) - wordAverage) / standardDev
            # print(zScore)
            if zScore > ZSCORELIMIT:
                subWordMarkerList.append(currKey)

    wordMarkerList.append(subWordMarkerList)

print(wordMarkerList)
