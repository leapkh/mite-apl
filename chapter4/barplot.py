from matplotlib import pyplot

provinces = ['Phnom Penh', 'Siem Reap', 'Kampung Cham', 'Kandal', 'Battambang']
studentsCount = [5, 3, 9, 7, 1]

bars = pyplot.bar(provinces, studentsCount)
pyplot.title('MITE 2022 Students Place of Birth')
pyplot.xlabel('Provinces')
pyplot.ylabel('Number of Students')

for bar in bars:
    x = bar.get_x() + (bar.get_width() / 2)
    studentCount = bar.get_height()
    y = studentCount + 0.01
    pyplot.text(x, y, studentCount)

pyplot.show()