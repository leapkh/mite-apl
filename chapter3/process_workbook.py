import os
import glob
import pandas

# List all files in a 'data' directory
dataDirectory = os.path.join('./chapter3/raw-data/', '*.xlsx')
filePaths = glob.glob(dataDirectory)

# DataFrame for holding all sheets
data = pandas.DataFrame()

# Read 'Food Sales' sheet from each file
for filePath in filePaths:
    worksheet = pandas.read_excel(filePath, sheet_name=1)

    # Concatenate all sheets together
    data = pandas.concat([data, worksheet])

# Write the whole data to the new file
outputFilePath = './chapter3/prepared-data/food-sales.xlsx'
data.to_csv(outputFilePath)

print('The files have been merged and written to ', outputFilePath)