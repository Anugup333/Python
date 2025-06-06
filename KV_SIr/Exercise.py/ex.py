import numpy as np
a = np.arange(6).reshape(2,3)
b = np.arange(6).reshape(2,3)

c = np.sum([a,b],axis=1)
print(a)
print(b)
print(c)
