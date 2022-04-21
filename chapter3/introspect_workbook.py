import pandas

filePath = './chapter3/data/Food Sales.xlsx'

workbook = pandas.read_excel(filePath, sheet_name=None)
print('Number of worksheet:', len(workbook))
for worksheetName, worksheet in workbook.items():
    print(worksheetName)
    print('Number of row:', len(worksheet))
    print('Number of column:', len(worksheet.columns))

