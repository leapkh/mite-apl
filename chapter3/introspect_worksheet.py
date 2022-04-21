import pandas

filePath = './chapter3/data/Students.xlsx'

worksheet = pandas.read_excel(filePath)
print('Number of row:', len(worksheet))
print('Number of column:', len(worksheet.columns))