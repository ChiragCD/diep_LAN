import numpy, imageio

l = [[1 for i in range(2000)] for j in range(2000)]
arr = numpy.array(l)
for i in range(0, 2000, 20):
    arr[i] = numpy.array([0 for i in range(2000)])
    arr[:, i] = 0

imageio.imwrite("back.jpeg", arr)
