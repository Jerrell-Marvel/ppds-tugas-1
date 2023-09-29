# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:55:27 2023

@author: Jerrell Marvel
"""

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


###############
# wordMarkerList = []

# for i in range(0, len(wordFreqList)) :
#     subWordMarkerList = []

#     for currKey in wordFreqList[i].keys():
#         isMarker = True
#         for wordFreq in wordFreqList[:i]:
#             if(wordFreq.get(currKey) != None):
#                 isMarker = False
#                 break

#         for wordFreq in wordFreqList[i+1:]:
#              if(wordFreq.get(currKey) != None):
#                  isMarker = False
#                  break

#         if isMarker == True:
#             subWordMarkerList.append(currKey)

#     wordMarkerList.append(subWordMarkerList)

# print(wordMarkerList)

################


#####################
# THRESHOLD = 100
# use average
# wordMarkerList = []
# wordFreqAvgDict = {}

# for currWordFreq in wordFreqList :
#     subWordMarkerList = []

#     for currKey in currWordFreq.keys():
#         wordAverage = wordFreqAvgDict.get(currKey)

#         if wordAverage == None :
#             totalFreq = 0
#             for wordFreq in wordFreqList :
#                 tempWordFreq = wordFreq.get(currKey)
#                 if(tempWordFreq != None):
#                     totalFreq += tempWordFreq
#             wordAverage = totalFreq / len(wordFreqList)
#             wordFreqAvgDict[currKey] = wordAverage

#         if currWordFreq[currKey] > wordAverage + THRESHOLD:
#             subWordMarkerList.append(currKey)

#     wordMarkerList.append(subWordMarkerList)

# print(wordMarkerList)
# print(wordFreqAvgDict)
#########################

# OUTLIER
wordMarkerList = []
wordFreqAvgDict = {}
wordStandardDevDict = {}

for currWordFreq in wordFreqList:
    subWordMarkerList = []

    for currKey in currWordFreq.keys():
        wordAverage = wordFreqAvgDict.get(currKey)
        standardDev = wordStandardDevDict.get(currKey)

        if wordAverage == None:
            standardDev = 0.0
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

                standardDev = standardDev + \
                    math.pow(tempWordFreq - wordAverage, 2)

            standardDev = math.sqrt(standardDev / len(wordFreqList))
            wordStandardDevDict[currKey] = standardDev

        if standardDev != 0:
            zScore = abs((currWordFreq[currKey] - wordAverage) / standardDev)
            # print(zScore)
            if zScore > 2:
                subWordMarkerList.append(currKey)

    wordMarkerList.append(subWordMarkerList)

# print(wordMarkerList)
# print(wordFreqAvgDict)

print(len(wordFreqAvgDict.keys()))
print(len(wordStandardDevDict.keys()))
