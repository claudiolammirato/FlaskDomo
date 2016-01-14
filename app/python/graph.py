import numpy
from matplotlib import pyplot

def plot(image):
    x = numpy.linspace(0, 10)
    y = numpy.cos(x)
    pyplot.plot(x, y)
    pyplot.savefig(image, format='png', transparent=True)
