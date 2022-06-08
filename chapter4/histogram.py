from matplotlib import pyplot
from numpy import random

ages = random.uniform(0, 120, 16000)

pyplot.hist(ages, rwidth=0.9, bins=12)
pyplot.title('Cambodia Population by Age in 2020')
pyplot.xlabel('Age')
pyplot.ylabel('Number of Population')
pyplot.show()