from matplotlib import pyplot
import numpy
numpy

ages = numpy.random.randint(0, 120, 1000)
pyplot.boxplot(ages)
pyplot.title('Age summary of Cambodian in 2020')
pyplot.show()