import sy
import numpy as np
arr=np.random.random((5,4))
print(np.matrix(arr))
for i in arr:
	if i>50:
		i=100
		continue
print(np.matrix(arr))		