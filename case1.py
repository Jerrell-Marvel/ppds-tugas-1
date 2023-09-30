# =================================
# Nikolas Giovanni (6182201009)
# Christian Hadinata (6182201020)
# Jerrell Marvel (6182201035)
# =================================

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

print(wordFreqList)
