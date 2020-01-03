import numpy as np
import matplotlib.pyplot as plt

f = open('Data.dat', 'w')

n = int(input("Enter number of Points:"))
d = int(input("Enter number of Dimension :"))
c = int(input("Enter number of Cluster :"))

random_matrix_array = np.random.rand(n, d) * 1000
print(random_matrix_array)

f.write(" dimension = " + str(d) + ";\n")
f.write(" nbPoints = " + str(n) + ";\n")
f.write(" nbCluster = " + str(c) + ";\n")
f.write("\n")

f.write(" points  = ")
f.write(str(random_matrix_array.tolist()))
f.write(";")
f.close()
plt.scatter(random_matrix_array[:, 0],random_matrix_array[:, 1])
print(random_matrix_array[:, 0])
print(random_matrix_array[:, 1])

plt.title('Nuage de points')
plt.xlabel('x1')
plt.ylabel('x2')

plt.savefig('Points.png')
plt.show()
