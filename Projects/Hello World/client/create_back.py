import numpy, imageio

l = [[1 for i in range(10000)] for j in range(10000)]
arr = numpy.array(l)
for i in range(0, 10000, 10):
    arr[i] = numpy.array([0 for i in range(10000)])
    arr[:, i] = 0

imageio.imwrite("back.jpeg", arr)
