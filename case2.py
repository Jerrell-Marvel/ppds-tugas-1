import glob

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

#####################
# AVERAGE
THRESHOLD = 0
wordMarkerList = []
wordFreqAvgDict = {}

for currWordFreq in wordFreqList:
    subWordMarkerList = []

    for currKey in currWordFreq.keys():
        wordAverage = wordFreqAvgDict.get(currKey)

        if wordAverage == None:
            totalFreq = 0
            for wordFreq in wordFreqList:
                tempWordFreq = wordFreq.get(currKey)
                if (tempWordFreq != None):
                    totalFreq += tempWordFreq
            wordAverage = totalFreq / len(wordFreqList)
            wordFreqAvgDict[currKey] = wordAverage

        if currWordFreq[currKey] > wordAverage + THRESHOLD:
            subWordMarkerList.append(currKey)

    wordMarkerList.append(subWordMarkerList)

print(wordMarkerList)
# print(wordFreqAvgDict)
