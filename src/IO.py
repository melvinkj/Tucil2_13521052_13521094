import random
import math
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def splashScreen():
    print("Welcome to closest pair program :D\n")

def mainMenu():
    print("""
        Choose:
        1. Generate random points
        2. File input
        3. Exit
    """)

def algorithmMenu():
    print("""
        Choose the algorithm to find closest pair:
        1. Divide and Conquer
        2. Brute Force
    """)

# TODO: Input validation gatau masih kurang atau ga
def inputHandler():
    while True:
        nPoints = int(input("Enter the n points you want to generate: "))
        if (nPoints >= 2):
            break
        print("Your input of n points is not valid. Please input a number with a minimum of two!")
    while True:
        nDims = int(input("Enter the d dimension of points you want to generate: "))
        if (nDims > 0):
            break
        print("Your input of d dimensions is not valid. Please input a number with a minimum of one!")
    return nPoints, nDims

# TODO: Input from file validation? blm tau perlu atau ga
def readFromFile(fileName):
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(dir_path + "\\test\\" + fileName + ".txt", "r")
    lines = f.readlines()
    points = [list(map(int, line.strip().split())) for line in lines]
    print(points)
    f.close()
    return points

def generateRandomPoints(total_points, total_dim) :
    points = [[0 for j in range (total_dim)] for i in range(total_points)]

    for i in range (total_points) :
        for j in range (total_dim) :
            points[i][j] = random.randint(-100, 100)
    
    print(points)
    return points

def visualize(points, pairs) :
    # length = len(points)
    # print(type(pairs))
    # print(pairs[0][0][0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in points:
        # if(x == p1[0] and y == p1[1] and z == p1[2]) or (x == p2[0] and y == p2[1] and z == p2[2]) :
        #     ax.scatter(x,y,z, c='b', marker='o')
        # else:
        #     ax.scatter(x,y,z, c='r', marker='o')
        isPair = False
        i = 0
        while (not isPair and i < len(pairs)):
            if(x == (pairs[i][0][0]) and y == pairs[i][0][1] and z == pairs[i][0][2]) or (x == pairs[i][1][0] and y == pairs[i][1][1] and z == pairs[i][1][2]):
                isPair = True
            else :
                i += 1
        if (isPair):
            ax.scatter(x,y,z, c=i, marker='o')
        else :
            ax.scatter(x,y,z, c='r', marker='o')


    plt.show()