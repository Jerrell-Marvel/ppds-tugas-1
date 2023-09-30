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

##################################################################
wordMarkerList = []

for i in range(0, len(wordFreqList)):
    subWordMarkerList = []

    for currKey in wordFreqList[i].keys():
        isMarker = True
        for wordFreq in wordFreqList[:i]:
            if (wordFreq.get(currKey) != None):
                isMarker = False
                break

        if (isMarker == True):
            for wordFreq in wordFreqList[i+1:]:
                if (wordFreq.get(currKey) != None):
                    isMarker = False
                    break

        if isMarker == True:
            subWordMarkerList.append(currKey)

    wordMarkerList.append(subWordMarkerList)

print(wordMarkerList)
