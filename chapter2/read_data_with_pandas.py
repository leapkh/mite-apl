import pandas

filePath = './chapter2/data/data-with-pandas.csv'
outputFilePath = './chapter2/data/prepared-data-with-pandas.csv'

dataFrame = pandas.read_csv(filePath)
### Filter rows by meeting a condition
#dataFrame['Price'] = dataFrame['Price'].astype(int)
#filterredDataFrame = dataFrame.loc[dataFrame['Price'] > 600]

### Filter rows by a set of interests
dataFrame['Year'] = dataFrame['Year'].astype(int)
filterredDataFrame = dataFrame.loc[dataFrame['Year'].isin([2017, 2018, 2019])]

filterredDataFrame.to_csv(outputFilePath, index=False)

print('The data has been filterred and written successfully.')