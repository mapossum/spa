import numpy as np

myA = np.array([0,1,2,3,0,1,2,3,0])

print myA

b = np.where(myA != 0)

print myA[b]
