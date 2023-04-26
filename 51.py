import numpy as np
from scipy import linalg

A=np.array[[1,2,3],[4,5,6],[8,9,0]]

detr=linalg.det(A)
print(detr)

inverse=linalg.inv(A)
print(inverse)