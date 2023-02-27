import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import IO
import Utils

# def generateRandomPoints(total_points) :
#     points = [[0, 0, 0] for i in range(total_points)]

#     for i in range (total_points) :
#         for j in range (3) :
#             points[i][j] = random.randint(-100, 100)
    
#     print(points)
#     return points

# def getDistance(p1, p2):
#     distance = math.sqrt(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2))
#     return distance

# def sorting(points) :


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

def bruteForce(points):
    # points = IO.generateRandomPoints(10)

    # closestPairs = np.array([[]])
    # for i in range(len(points)):
    #     for j in range(i+1, len(points)):
    #         if (i == 0 and j ==1):
    #             shortestDistance = Utils.getDistancePoints(points[i], points[j])
    #             closestPairs = np.append(closestPairs,[points[i], points[j]])
    #         else :
    #             if (Utils.getDistancePoints(points[i], points[j]) < shortestDistance):
    #                 shortestDistance = Utils.getDistancePoints(points[i], points[j])
    #                 closestPairs = np.array([points[i], points[j]])
    #             elif (Utils.getDistancePoints(points[i], points[j]) < shortestDistance):
    #                 closestPairs = np.append(closestPairs, [points[i], points[j]])
    # print("Closest pair:")
    # print(closestPairs)      
    # return closestPairs, shortestDistance 

    closestPairs = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (i == 0 and j ==1):
                shortestDistance = Utils.getDistancePoints(points[i], points[j])
                closestPairs += [[points[i], points[j]]]
            else :
                if (Utils.getDistancePoints(points[i], points[j]) < shortestDistance):
                    closestPairs = []
                    shortestDistance = Utils.getDistancePoints(points[i], points[j])
                    closestPairs = [[points[i], points[j]]]
                elif (Utils.getDistancePoints(points[i], points[j]) == shortestDistance):
                    closestPair = [points[i], points[j]]
                    closestPairs = Utils.appendIfNotSame(closestPairs, closestPair)
    # print("Closest pair:")
    # print(closestPairs)      
    return closestPairs, shortestDistance 