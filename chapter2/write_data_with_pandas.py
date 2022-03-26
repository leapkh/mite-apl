from pandas.core.frame import DataFrame

data = {
    'ID': ['1', '2', '3'],
    'Name': ['Samsung Galaxy Note 20', 'Apple iPhone 11, 256G', 'Oppo Reno 2'],
    'Price': ['669', '829', '500'],
    'Year': ['2020', '2019', '2020']
}

filePath = './chapter2/data/data-with-pandas.csv'

dataFrame = DataFrame(data)
dataFrame.to_csv(filePath, index=False)
print('The data has been written successfully.')