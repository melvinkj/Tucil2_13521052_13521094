import IO
from DivideAndConquer import findClosestPair
import numpy as np

def algorithmChooser(inputPoints):
    while True:
        IO.algorithmMenu()
        opt = int(input("Enter your option: "))
        if (opt == 1):
            points = np.array(inputPoints)
            closestPair, closestDist = findClosestPair(points, len(inputPoints))
            print("Closest pair of points:", closestPair, "\n")
            print("Closest distance is:", closestDist)
            if (len(inputPoints[0]) == 3):
                IO.visualize(inputPoints, closestPair[0], closestPair[1])
            break
        elif (opt == 2):
            #Masukkin algoritma brute force di sini
            break
        print("Your option is not valid!\n")

def main():
    IO.splashScreen()
    IO.mainMenu()
    opt = int(input("Enter your option: "))
    while (opt != 3):
        if (opt == 1):
            nPoints, nDims = IO.inputHandler()
            print("Here is your random points: \n")
            randPoints = IO.generateRandomPoints(nPoints, nDims)
            algorithmChooser(randPoints)
        elif (opt == 2):
            fileName = input("Enter your file name without .txt: ")
            filePoints = IO.readFromFile(fileName)
            algorithmChooser(filePoints)
        else:
            print("Option not validdd \n")
        IO.mainMenu()
        opt = int(input("Enter your option: "))

if __name__=="__main__":
    main()
