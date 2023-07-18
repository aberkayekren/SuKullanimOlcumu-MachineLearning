import os

trainFolder = []
testFolder = []

def csvList(filePath):
    fileList = []

    for folder in os.listdir(filePath):
        if folder.endswith(".csv"):
            fileList.append(folder)
    for string in fileList:
        if len(trainFolder) < len(fileList) * 0.8:
            trainFolder.append(string)
        else:
            testFolder.append(string)
    return fileList

filePath = "Your File Path"
csvFile = csvList(filePath)
print(csvFile)
print("Train Folder:", trainFolder)
print("Test Folder:", testFolder)