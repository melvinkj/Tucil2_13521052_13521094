import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generateRandomPoints(total_points) :
    points = [[0, 0, 0] for i in range(total_points)]

    for i in range (total_points) :
        for j in range (3) :
            points[i][j] = random.randint(-100, 100)
    
    print(points)
    return points

def visualize(points, p1, p2) :
    # length = len(points)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in points:
        if(x == p1[0] and y == p1[1] and z == p1[2]) or (x == p2[0] and y == p2[1] and z == p2[2]) :
            ax.scatter(x,y,z, c='b', marker='o')
        else:
            ax.scatter(x,y,z, c='r', marker='o')

    plt.show()