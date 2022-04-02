import pandas

filePath = './chapter2/data/phones.csv'
outputFilePath = './chapter2/data/filterred-columns-using-pandas.csv'

dataFrame = pandas.read_csv(filePath, on_bad_lines='warn')

filterredDataFrame = dataFrame.iloc[:, [0, 1, 12]]
filterredDataFrame.to_csv(outputFilePath)

print(str(filterredDataFrame.count) + ' columns have been filterred.')