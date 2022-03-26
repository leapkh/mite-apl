import csv

filePath = './chapter2/data/data-with-csv.csv'
outputFilePath = './chapter2/data/prepared-data-with-csv.csv'

with open(filePath, 'r') as fileReader:
    csvReader = csv.reader(fileReader)

    with open(outputFilePath, 'w') as fileWriter:
        csvWriter = csv.writer(fileWriter)
        header = next(csvReader)
        csvWriter.writerow(header)
        for row in csvReader:
            ### Filter rows by meeting a condition
            #price = int(row[2])
            #if(price > 600):
                #csvWriter.writerow(row)

            ### Filter rows by a set of interests
            year = row[3]
            if(year in ['2017', '2018', '2019']):
                csvWriter.writerow(row)

print('The data has been filterred and written successfully.')
        