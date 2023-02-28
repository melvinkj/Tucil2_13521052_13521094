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
     ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝  \033[00m""")

def mainMenu():
    print("""
==============================
\033[31m************\033[00m\033[34m MENU \033[00m\033[31m************\033[00m
==============================
1. Generate Random Points
2. File Input
3. Exit
    """)

# def algorithmMenu():
#     print("""
#         Choose the algorithm to find closest pair:
#         1. Divide and Conquer
#         2. Brute Force
#     """)

def saveConfirmation(nPoints, nDims, points, closestPairsDNC, closestDistDNC, elapsed_timeDNC, ctrOptDNC, closestPairsBF, closestDistBF, elapsed_timeBF, ctrOptBF):
    save = input("\nDo you want to save the result to a .txt file (Y/N)? ")

    while (save != "Y" and save!= "y" and save!= "N" and save != "n"):
        print("\033[31mYour input is not valid. Please enter a valid input!\033[00m")
        save = input("Do you want to save the result to a .txt file (Y/N)? ")

    if (save == "Y" or save == "y") :
        fileName = input("The result will be saved to a file. Enter your desired file name: ")
        writeToFile(nPoints, nDims, fileName, points, closestPairsDNC, closestDistDNC, elapsed_timeDNC, ctrOptDNC, closestPairsBF, closestDistBF, elapsed_timeBF, ctrOptBF)

def writePairsToFile(f, pairs):
    f.write("Closest Pair(s) of Points: \n")
    for i in range (len(pairs)):
        f.write("\t" + str(i+1) + ". " + Utils.formatPoint(pairs[i][0]) + " - " + Utils.formatPoint(pairs[i][1]) + "\n")

def writeToFile(nPoints, nDims, fileName, points, closestPairsDNC, closestDistDNC, elapsed_timeDNC, ctrOptDNC, closestPairsBF, closestDistBF, elapsed_timeBF, ctrOptBF):
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    f = open(dir_path + "\\output\\" + fileName + ".txt", "w")
    f.write("Number of Points               : " + str(nPoints)+ "\n")
    f.write("Dimension                      : " + str(nDims)+ "\n")
    f.write("Points                         : " + str(points) + "\n")

    # Result by Divide and Conquer
    f.write("\n=========== DIVIDE AND CONQUER ===========\n")
    writePairsToFile(f, closestPairsDNC)
    f.write("Closest Distance               : " + str(closestDistDNC) + "\n")
    f.write("Number of Euclidean Operations : " + str(ctrOptDNC)+ "\n")
    f.write("Execution Time                 : " + str(elapsed_timeDNC) + " ms\n")

    # Result by Brute Force
    f.write("\n=============== BRUTE FORCE ===============\n")
    writePairsToFile(f, closestPairsBF)
    f.write("Closest Distance               : " + str(closestDistBF) + "\n")
    f.write("Number of Euclidean Operations : " + str(ctrOptBF)+ "\n")
    f.write("Execution Time                 : " + str(elapsed_timeBF) + " ms\n")
    f.close()

def inputHandler():
    while True:
        try:
            nPoints = int(input("Enter the n points you want to generate: "))
        except: 
            print("\033[31mYour input of n points is not valid. Please input a number with a minimum of two!\033[00m")
            continue
        if (nPoints >= 2):
            break
        print("\033[31mYour input of n points is not valid. Please input a number with a minimum of two!\033[00m")
    while True:
        try:
            nDims = int(input("Enter the d dimension of points you want to generate: "))
        except:
            print("\033[31mYour input of n points is not valid. Please input a number with a minimum of two!\033[00m")
            continue

        if (nDims > 0):
            break
        print("\033[31mYour input of d dimensions is not valid. Please input a number with a minimum of one!\033[00m")
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
    print("Closest Pair(s) of Points:")
    for i in range (len(pairs)):
        print("\t" + str(i+1) + ". \033[94m" + Utils.formatPoint(pairs[i][0]) + "\033[00m - \033[93m" + Utils.formatPoint(pairs[i][1]) + "\033[00m")

