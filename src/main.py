import IO
from DivideAndConquer import findClosestPair
from BruteForce import bruteForce
import numpy as np
import time
import Utils

def executeDivideAndConquer(inputPoints):
    ctrOpt = 0
    start = time.time()
    closestPairs, closestDist, ctrOpt = findClosestPair(inputPoints, len(inputPoints), len(inputPoints[0]), ctrOpt)
    end = time.time()
    elapsed_time = (end - start) * 1000  # in milliseconds
    IO.printPairs(closestPairs)
    print("Closest Distance                 :\033[92m", closestDist, "\033[00m")
    print("Number of Euclidean Operations   :\033[91m", ctrOpt, "\033[00m")
    print("Execution Time                   :\033[35m", elapsed_time, "ms\033[00m")
    if (len(inputPoints[0]) == 3):
        IO.visualize(inputPoints, closestPairs)

    return closestPairs, closestDist, elapsed_time, ctrOpt

def executeBruteForce(inputPoints):
    ctrOpt = 0
    points = inputPoints
    start = time.time()
    closestPairs, closestDist, ctrOpt = bruteForce(points, ctrOpt)
    end = time.time()
    elapsed_time = (end - start) * 1000  # in milliseconds
    IO.printPairs(closestPairs)
    print("Closest Distance                 :\033[92m", closestDist, "\033[00m")
    print("Number of Euclidean Operations   :\033[91m", ctrOpt, "\033[00m")
    print("Execution Time                   :\033[35m", elapsed_time, "ms\033[00m")

    if (len(inputPoints[0]) == 3):
        IO.visualize(inputPoints, closestPairs)
            
    return closestPairs, closestDist, elapsed_time, ctrOpt

def main():
    IO.splashScreen()
    IO.mainMenu()
    opt = int(input("Enter your choice: "))
    while (opt != 3):
        if (opt == 1 or opt == 2):
            if (opt == 1):
                nPoints, nDims = IO.inputHandler()
                print("Here are your random points: \n")
                points = Utils.generateRandomPoints(nPoints, nDims)

            elif (opt == 2):
                fileName = input("Enter your file name without .txt: ")
                points = IO.readFromFile(fileName)
                nPoints, nDims = len(points) , len (points[0])

            # Divide and Conquer
            print("\n\033[31m=========== \033[00m\033[36mDIVIDE AND CONQUER\033[00m\033[31m ===========\033[00m")
            closestPairsDNC, closestDistDNC, elapsed_timeDNC, ctrOptDNC = executeDivideAndConquer(points)

            # Brute Froce
            print("\n\033[96m=============== \033[00m\033[31mBRUTE FORCE\033[00m\033[36m ===============\033[00m")
            closestPairsBF, closestDistBF, elapsed_timeBF, ctrOptBF = executeBruteForce(points)

            # Saving Result to A File
            IO.saveConfirmation(nPoints, nDims, points, closestPairsDNC, closestDistDNC, elapsed_timeDNC, ctrOptDNC, closestPairsBF, closestDistBF, elapsed_timeBF, ctrOptBF)

    
        else:
            print("\033[31mInvalid input! \033[00m \n")
        
        IO.mainMenu()
        opt = int(input("Enter your choice: "))

if __name__=="__main__":
    main()
