import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[5,6,7,8],[1,2,3,4]])
print("First array is: ",a)
print("Second array: ",b)
if np.array_equal(a,b):
	print("Equal")
else:
	print("Not Equal")
	

