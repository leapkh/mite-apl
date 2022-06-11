import pandas
from matplotlib import pyplot

studentsByGradeDf = pandas.DataFrame({
    'Grade': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Number of Students': [89, 391, 1528, 42843, 72100, 3280]
})

studentsByGradeDf.plot(kind = 'bar', x = 'Grade', y = 'Number of Students')
pyplot.grid()
pyplot.title('BacII 2021 by Grades')
pyplot.show()