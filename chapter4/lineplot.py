from matplotlib import pyplot

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
gdps = [1500, 1578, 1612, 1615, 1673, 1200, 1150]

pyplot.plot(years, gdps)
pyplot.title('Cambodia GDP from 2015 to 2021')
pyplot.xlabel('Year')
pyplot.ylabel('GDP')
pyplot.grid()
pyplot.show()