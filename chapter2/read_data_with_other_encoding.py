import pandas

filePath = './chapter2/data/meetingAttendanceList.csv'

dataFrame = pandas.read_csv(filePath, encoding='utf-16')

print(dataFrame)