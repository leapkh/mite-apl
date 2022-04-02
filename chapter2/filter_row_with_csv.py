import csv
import re

filePath = './chapter2/data/phones.csv'
outputFilePath = './chapter2/data/filterred-phones-using-csv.csv'

fileReader = open(filePath, 'r')
csvReader = csv.reader(fileReader)

fileWriter = open(outputFilePath, 'w')
csvWriter = csv.writer(fileWriter)

# Write header
#csvWriter.writerow(next(csvReader))

# Concition 1: Filter only phones which have 'announced' value only year (only 4 digits otherwise NO)
conditionPattern = re.compile(r'^[0-9]{4}$')
# Condition 2: Filter only phones which have 'memory_card' as microSD with 256 GB (start with microSD follow by anything with any number of copies and 256 GB)
conditionPattern2 = re.compile(r'^microSD.*256\sGB')

count = 0
for row in csvReader:
    announced = row[9].strip()
    memoryCard = row[22].strip()

    if(conditionPattern.search(announced) and conditionPattern2.search(memoryCard)):
        csvWriter.writerow(row)
        count += 1

fileReader.close()
fileWriter.close()

print(str(count) + ' rows found.')