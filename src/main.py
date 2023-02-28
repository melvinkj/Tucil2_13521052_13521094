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
            ctrOpt = 0
            start = time.time()
            closestPairs, closestDist, ctrOpt = findClosestPair(inputPoints, len(inputPoints), len(inputPoints[0]), ctrOpt)
            end = time.time()
            elapsed_time = (end - start) * 1000  # in milliseconds
            print("Closest pair(s) of points:", closestPairs, "\n")
            print("Closest distance is:", closestDist)
            print("Number of Euclidean operations:", ctrOpt)
            print("\nExecution time: ", elapsed_time, "milliseconds")
            if (len(inputPoints[0]) == 3):
                IO.visualize(inputPoints, closestPairs)
            break
        elif (algorithmOpt == 2):
            #Masukkin algoritma brute force di sini
            ctrOpt = 0
            points = inputPoints
            start = time.time()
            closestPairs, closestDist, ctrOpt = bruteForce(points, ctrOpt)
            end = time.time()
            elapsed_time = (end - start) * 1000  # in milliseconds
            print("Closest pair(s) of points:", closestPairs, "\n")
            print("Closest distance is:", closestDist)
            print("Number of Euclidean operations:", ctrOpt)
            print("\nExecution time: ", elapsed_time, "milliseconds")

            if (len(inputPoints[0]) == 3):
                IO.visualize(inputPoints, closestPairs)
            break
        print("\033[31mInvalid input! \033[00m \n")
    return algorithmOpt, closestPairs, closestDist, elapsed_time, ctrOpt

def main():
    IO.splashScreen()
    IO.mainMenu()
    opt = int(input("Enter your choice: "))
    while (opt != 3):
        if (opt == 1):
            nPoints, nDims = IO.inputHandler()
            print("Here is your random points: \n")
            randPoints = IO.generateRandomPoints(nPoints, nDims)
            algorithmOpt, closestPairs, closestDist, elapsed_time, ctrOpt = algorithmChooser(randPoints)
            IO.saveConfirmation(nPoints, nDims, algorithmOpt, randPoints, closestPairs, closestDist, elapsed_time, ctrOpt)
        elif (opt == 2):
            fileName = input("Enter your file name without .txt: ")
            filePoints = IO.readFromFile(fileName)
            algorithmOpt, closestPairs, closestDist, elapsed_time, ctrOpt = algorithmChooser(filePoints)
            IO.saveConfirmation(nPoints, nDims, algorithmOpt, filePoints,closestPairs, closestDist, elapsed_time, ctrOpt)
        else:
            print("\033[31mInvalid input! \033[00m \n")
        
        

        IO.mainMenu()
        opt = int(input("Enter your choice: "))

if __name__=="__main__":
    main()
