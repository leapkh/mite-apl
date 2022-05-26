import glob
import os
import pandas

### Combine Shop A records

# List all files from Shop A
desiredFiles = os.path.join('./midterm/data/Shop A', '*.xlsx')
filePaths = glob.glob(desiredFiles)

# Read data from each file and combine
shopA = pandas.DataFrame()
for filePath in filePaths:
    sheet = pandas.read_excel(filePath)
    shopA = pandas.concat([shopA, sheet])

# Add shop name column
shopA['Shop Name'] = 'Shop A'

# Filter columns
shopA = shopA.iloc[:, [7, 3, 4, 6, 5]]

# Rename column
shopA = shopA.rename(columns={'Laptop Brand': 'Brand', 'Laptop Model': 'Model'})

############################################

### Combine Shop B records

# List all files from Shop B
desiredFiles = os.path.join('./midterm/data/Shop B', '*.xlsx')
filePaths = glob.glob(desiredFiles)

# Read data from each file and combine
shopB = pandas.DataFrame()
for filePath in filePaths:
    sheet = pandas.read_excel(filePath)
    shopB = pandas.concat([shopB, sheet])

# Add shop name and model column
shopB['Shop Name'] = 'Shop B'
shopB['Model'] = 'N/A'

# Filter columns
shopB = shopB.iloc[:, [6, 3, 7, 4, 5]]

# Rename column
shopB = shopB.rename(columns={'Laptop': 'Brand'})

############################################

### Combine Shop C records
# List all files from Shop C
desiredFiles = os.path.join('./midterm/data/Shop C', '*.*')
filePaths = glob.glob(desiredFiles)

# Read data from each file and combine
shopC = pandas.DataFrame()
for filePath in filePaths:
    if filePath.endswith('.xlsx'):
        sheet = pandas.read_excel(filePath)
        shopC = pandas.concat([shopC, sheet])
    elif filePath.endswith('.csv'):
        sheet = pandas.read_csv(filePath)
        shopC = pandas.concat([shopC, sheet])

# Add shop name and model column
shopC['Shop Name'] = 'Shop C'
shopC['Brand'] = ''
shopC['Model'] = ''

# Split Laptop column into Brand and Model
#shopC[['Laptop', 'Model']] = shopC.Laptop.str.split('-', expand = True)
rows = []
for index, row in shopC.iterrows():
    laptop = row['Laptop']
    brand, model = laptop.split('-')
    row['Brand'] = brand
    row['Model'] = model
    rows.append(row)

shopC = pandas.DataFrame(rows)

# Filter columns
shopC = shopC.iloc[:, [6, 7, 8, 5, 4]]

############################################

# Combine all shops together
allRecords = pandas.concat([shopA, shopB, shopC])

# Calculate average price
averagePrice = allRecords['Price'].mean()
print('The average latop price is:', averagePrice)

# Add average below the records
averageDataFrame = pandas.DataFrame({'Model': ['Average'], 'Price': [averagePrice]})
allRecords = pandas.concat([allRecords, averageDataFrame])

# Write data to CSV file
outputFilePath = './midterm/data/Output.csv'
allRecords.to_csv(outputFilePath)




