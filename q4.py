import sys
import numpy as np
arr=np.random(10)
i=1
for arr[i] in arr:
	arr[i]=-10
	i=i+2
print(np.matrix(arr)