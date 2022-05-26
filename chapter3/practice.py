import os
import glob
import pandas

outputFilePath = './chapter3/prepared-data/food-sales.xlsx'
wholeData = pandas.DataFrame()

# List all file paths from the folder 'data2'
desiredFiles = os.path.join('./chapter3/data2', '*.xlsx')
filePaths = glob.glob(desiredFiles)

# Read data from 'FoodSales' sheet of each file
for filePath in filePaths:
    foodSalesSheet = pandas.read_excel(filePath, 'FoodSales')

    # Combine all sheet together
    wholeData = pandas.concat([wholeData, foodSalesSheet])

# Write the whole data into new file.
wholeData.to_excel(outputFilePath)
print('The files have been merged and written successfully to', outputFilePath)