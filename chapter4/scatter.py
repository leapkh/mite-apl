from matplotlib import pyplot

speeds = [70, 120, 10, 30, 90]
durationInMinutes = [90, 50, 240, 170, 72]

pyplot.scatter(x = speeds, y = durationInMinutes)
pyplot.xlabel('Speed in km/h')
pyplot.ylabel('Duration in minute')
pyplot.title('Transportation from Phnom Penh to Oudong')
pyplot.show()