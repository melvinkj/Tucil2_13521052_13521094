import os
import matplotlib.pyplot as plt
import Utils

def splashScreen():
    print("\033[32mWelcome to closest pair program :D\033[00m\n")
    print("""\033[34m
     ██████╗██╗      ██████╗ ███████╗███████╗███████╗████████╗    ██████╗  █████╗ ██╗██████╗ ███████╗
    ██╔════╝██║     ██╔═══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
    ██║     ██║     ██║   ██║███████╗█████╗  ███████╗   ██║       ██████╔╝███████║██║██████╔╝███████╗
    ██║     ██║     ██║   ██║╚════██║██╔══╝  ╚════██║   ██║       ██╔═══╝ ██╔══██║██║██╔══██╗╚════██║
    ╚██████╗███████╗╚██████╔╝███████║███████╗███████║   ██║       ██║     ██║  ██║██║██║  ██║███████║
    ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝                                                                                                                         
   \033[00m""")

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

def saveConfirmation(nPoints, nDims, opt, points, closestPairs, closestDist, elapsed_time, ctrOpt):
    save = input("Do you want to save the result to a .txt file (Y/N)? ")

    while (save != "Y" and save!= "y" and save!= "N" and save != "n"):
        print("Your input is not valid. Please enter a valid input!")
        save = input("Do you want to save the result to a .txt file (Y/N)? ")

    if (save == "Y" or save == "y") :
        fileName = input("The result will be saved to a file. Enter your desired file name: ")
        writeToFile(nPoints, nDims, opt, fileName, points, closestPairs, closestDist, elapsed_time, ctrOpt)

def writePairsToFile(f, pairs):
    f.write("Closest pair(s) of points: \n")
    for i in range (len(pairs)):
        f.write("\t" + str(i+1) + ". " + Utils.formatPoint(pairs[i][0]) + " - " + Utils.formatPoint(pairs[i][1]) + "\n")
    f.write("\n")

def writeToFile(nPoints, nDims, opt, fileName, points, closestPairs, closestDist, elapsed_time, ctrOpt):
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(dir_path + "\\output\\" + fileName + ".txt", "w")
    f.write("Number of Points: " + str(nPoints)+ "\n")
    f.write("Dimension: " + str(nDims)+ "\n")
    f.write("Points: " + str(points) + "\n")
    f.write("Algorithm: " + ("Divide and Conquer" if opt == 1 else "Brute Force") + "\n")
    writePairsToFile(f, closestPairs)
    f.write("Closest Distance: " + str(closestDist) + "\n")
    f.write("Number of Euclidean operations:" + str(ctrOpt))
    f.write("Execution Time: " + str(elapsed_time) + " milliseconds\n")
    f.close()

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

def readFromFile(fileName):
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(dir_path + "\\test\\" + fileName + ".txt", "r")
    lines = f.readlines()
    points = [list(map(int, line.strip().split())) for line in lines]
    print(points)
    f.close()
    return points

def visualize(points, pairs) :
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for x, y, z in points:
        isPair = False
        i = 0
        color = ['blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'tab:orange', 'tab:olive']
        while (not isPair and i < len(pairs)):
            if(x == (pairs[i][0][0]) and y == pairs[i][0][1] and z == pairs[i][0][2]) or (x == pairs[i][1][0] and y == pairs[i][1][1] and z == pairs[i][1][2]):
                isPair = True
            else :
                i += 1
        if (isPair):
            ax.scatter(x,y,z, c=color[(i%8)], marker='o')
        else :
            ax.scatter(x,y,z, c='r', marker='o')

    plt.show()

def printPairs(pairs):
    print("Closest pair(s) of points: ")
    for i in range (len(pairs)):
        print("\t" + str(i+1) + ". " + Utils.formatPoint(pairs[i][0]) + " - " + Utils.formatPoint(pairs[i][1]))

    print("\n")
