# reshape in numpy
import numpy as np
lst = list(map(int,input().split()))
arr = np.array(lst)

out = arr.reshape(6,2)
print(arr)
print(out)
