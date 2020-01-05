import numpy as np
import matplotlib.pyplot as plt

f = open('Data.dat', 'w')

n = int(input("Enter number of Points:"))
d = int(input("Enter number of Dimension :"))
c = int(input("Enter number of Cluster :"))


random_points_array = np.random.rand(n, d) * 1000
print(random_points_array)

Distance_array =[]


def distance(p1, p2):
    return np.linalg.norm(p1-p2)


for p1 in random_points_array:
    temp_array=[]
    for p2 in random_points_array:
        temp_array.append(distance(p1,p2))
    Distance_array.append(temp_array)

print(Distance_array)

f.write(" dimension = " + str(d) + ";\n")
f.write(" nbPoints = " + str(n) + ";\n")
f.write(" nbCluster = " + str(c) + ";\n")
f.write("\n")

f.write(" points  = ")
f.write(str(random_points_array.tolist()))
f.write(";")

f.write("\n")

f.write(" distance  = ")
f.write(str(Distance_array))
f.write(";")

f.close()

"""

plt.scatter(random_points_array[:, 0],random_points_array[:, 1])
print(random_points_array[:, 0])
print(random_points_array[:, 1])

plt.title('Nuage de points')
plt.xlabel('x1')
plt.ylabel('x2')

plt.savefig('Points.png')
plt.show()
"""
