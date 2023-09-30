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
                        break

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
index = 0
for dictFrekFolder in wordFreqList:
    listBawah = wordFreqList[:index]
    listAtas = wordFreqList[index+1:]
    listMarkerSub = []
    for key in dictFrekFolder.keys():
        isMarker = True
        for dictFrekSub in listBawah:
            if (dictFrekSub.get(key) != None):
                isMarker = False
                break

        if (isMarker):
            for dictFrekSub2 in listAtas:
                if (dictFrekSub2.get(key) != None):
                    isMarker = False
                    break

        if (isMarker):
            listMarkerSub.append(key)
    wordMarkerList.append(listMarkerSub)
    index += 1

print(wordMarkerList)
