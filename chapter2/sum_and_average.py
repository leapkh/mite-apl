import pandas

filePath = './chapter2/data/filterred-columns-using-pandas.csv'

dataFrame = pandas.read_csv(filePath, on_bad_lines='warn')
condition = dataFrame['weight_g'].str.isnumeric() == True
filterredDataFrame = dataFrame.loc[condition]
totalWeight = filterredDataFrame['weight_g'].astype(int).sum()
averageWeight = filterredDataFrame['weight_g'].astype(int).mean()
print('Total weight: ' + str(totalWeight))
print('Average weight: ' + str(averageWeight))