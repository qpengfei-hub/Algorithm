import random
import numpy
a =numpy.array([[1,10],[2,5],[3,5],[4,5]])

p = 0
px = []
for i in range(len(a)):
    p +=a[i,1]
    px.append(p/24)
print(px)



n = []
while(len(n) < 3):
    m = [random.random() for i in range(len(a))]
    for i in range(len(a)):
        if px[i] > m[i]:
            n.append(a[i])
            break
print(n)