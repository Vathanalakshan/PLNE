f = open('Data.dat', 'w')
import numpy as np

n = int(input("Enter number of elements:"))
d = int(input("Enter number of Dimension :"))

random_matrix_array = np.random.rand(n, d)
print(random_matrix_array)

f.close()
