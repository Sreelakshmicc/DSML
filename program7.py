import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1]])
print("Array elements are:",a)
print("Sum of all elements:")
print(np.sum(a))


print("Sum of each column:")
print(np.sum(a, axis=0))

print("Sum of each row:")
print(np.sum(a, axis=1)) 

