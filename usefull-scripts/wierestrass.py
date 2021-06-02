import matplotlib.pyplot as plt
import numpy

ogr = 100000
#mhmm okey.
startA = -10
stopA = 10
A=numpy.arange(startA, stopA, ((stopA - startA)/ogr))   
print("Piła wirestrassa~wrrrum")
def pilaaaa(x, var):
    we = numpy.zeros(ogr)
    for n in range(var):
        we = we + numpy.cos(3**n*numpy.pi*x)/(2**n)
    return we

plt.plot(A, numpy.reshape(pilaaaa(A, 500), (ogr)))

plt.show()