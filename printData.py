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

#import pandas as pd
#import printFolderName as pfn

#def excel_to_dict(file_path):
    #data = pd.read_excel(file_path)
    #return data.to_dict('records')

# Örnek kullanım
#file_path = pfn.trainFolder[13]  # Okunacak Excel dosyasının yolunu belirtin
#result = excel_to_dict(file_path)
#values = [item[list(item)[-1]] for item in result]
#valuesOfDate = [item[list(item)[0]] for item in result]
#print(values[::-1])
