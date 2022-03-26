data = [
    ['ID', 'Name', 'Price', 'Year'],
    ['1', 'Samsung Galaxy Note 20', '669', '2020'],
    ['2', 'Apple iPhone 11, 256G', '829', '2019'],
    ['3', 'Oppo Reno 2', '510', '2020']
]

filePath = './chapter2/data/data-with-manual.csv'
with open(filePath, 'w') as fileWriter:
    for row in data:
        newRow = []
        for item in row:
            if(',' in item):
                item = '"' + item + '"'
            newRow.append(item)
        line = ','.join(newRow) + '\n'
        fileWriter.write(line)

print('The data has been written successfully.')