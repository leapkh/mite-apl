import pandas

filePath = './chapter2/data/phones.csv'
outputFilePath = './chapter2/data/filterred-phones-using-pandas.csv'

dataFrame = pandas.read_csv(filePath, on_bad_lines='warn')

# Concition 1: Filter only phones which have 'announced' value only year (only 4 digits otherwise NO)
filterCondition = dataFrame['announced'].str.isnumeric() == True
filterredDataFrame = dataFrame.loc[filterCondition]

filterCondition2 = filterredDataFrame['announced'].str.len() == 4
filterredDataFrame2 = filterredDataFrame[filterCondition2]

filterredDataFrame2.to_csv(outputFilePath)

print(str(filterredDataFrame2.count) + ' rows found.')