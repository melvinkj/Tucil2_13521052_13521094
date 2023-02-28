import IO
from DivideAndConquer import findClosestPair
from BruteForce import bruteForce
import numpy as np
import time

def algorithmChooser(inputPoints):
    while True:
        IO.algorithmMenu()
        algorithmOpt = int(input("Enter your choice: "))
        if (algorithmOpt == 1):
            points = np.array(inputPoints)
            start = time.time()
            closestPairs, closestDist = findClosestPair(points, len(inputPoints), len(inputPoints[0]))
            end = time.time()
            elapsed_time = (end - start) * 1000  # in milliseconds
            print("Closest pair of points:", closestPairs, "\n")
            print("Closest distance is:", closestDist)
            print("\nExecution time: ", elapsed_time, "milliseconds")
            if (len(inputPoints[0]) == 3):
                IO.visualize(inputPoints, closestPairs)
            break
        elif (algorithmOpt == 2):
            #Masukkin algoritma brute force di sini
            points = inputPoints
            start = time.time()
            closestPairs, closestDist = bruteForce(points)
            end = time.time()
            elapsed_time = (end - start) * 1000  # in milliseconds
            print("Closest pair(s) of points:", closestPairs, "\n")
            print("Closest distance is:", closestDist)
            print("\nExecution time: ", elapsed_time, "milliseconds")

            if (len(inputPoints[0]) == 3):
                IO.visualize(inputPoints, closestPairs)
            break
        print("\033[31mInvalid input! \033[00m \n")
    return algorithmOpt, closestPairs, closestDist, elapsed_time

def main():
    IO.splashScreen()
    IO.mainMenu()
    opt = int(input("Enter your choice: "))
    while (opt != 3):
        if (opt == 1):
            nPoints, nDims = IO.inputHandler()
            print("Here is your random points: \n")
            randPoints = IO.generateRandomPoints(nPoints, nDims)
            algorithmOpt, closestPairs, closestDist, elapsed_time = algorithmChooser(randPoints)
            IO.saveConfirmation(nPoints, nDims, algorithmOpt, randPoints, closestPairs, closestDist, elapsed_time)
        elif (opt == 2):
            fileName = input("Enter your file name without .txt: ")
            filePoints = IO.readFromFile(fileName)
            algorithmOpt, closestPairs, closestDist, elapsed_time = algorithmChooser(filePoints)
            IO.saveConfirmation(nPoints, nDims, algorithmOpt, filePoints,closestPairs, closestDist, elapsed_time)
        else:
            print("\033[31mInvalid input! \033[00m \n")
        
        

        IO.mainMenu()
        opt = int(input("Enter your choice: "))

if __name__=="__main__":
    main()
