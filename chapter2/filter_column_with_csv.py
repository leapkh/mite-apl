import csv
import re

filePath = './chapter2/data/phones.csv'
outputFilePath = './chapter2/data/filterred-column-using-csv.csv'

fileReader = open(filePath, 'r')
csvReader = csv.reader(fileReader)

fileWriter = open(outputFilePath, 'w')
csvWriter = csv.writer(fileWriter)

filterredColumns = [0, 1, 12]
for row in csvReader:
    newRow = []
    for index in filterredColumns:
        column = row[index]
        newRow.append(column)
    csvWriter.writerow(newRow)

fileReader.close()
fileWriter.close()

print(str(len(filterredColumns)) + ' columns have been filterred.')