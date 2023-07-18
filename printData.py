import csv
import printFolder as pf

def csvToDict(filePath):
    with open(filePath, 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        data = [row for row in reader]
    return data

filePath = pf.trainFolder["Path Index"]
result = csvToDict(filePath)
values = [item[list(item)[-1]] for item in result]
dates = [item[list(item)[0]] for item in result]
print(values[::-1])