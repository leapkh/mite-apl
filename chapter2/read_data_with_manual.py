filePath = './chapter2/data/data-with-manual.csv'

with open(filePath, 'r') as fileReader:
    for line in fileReader:
        attributes = line.split(',')
        print(attributes[0])
        print(attributes[1])
        print(attributes[2])
        print(attributes[3])