import random
import math

def generateRandomPoints(total_points) :
    points = [[0, 0, 0] for i in range(total_points)]

    for i in range (total_points) :
        for j in range (3) :
            points[i][j] = random.randint(-100, 100)
    
    print(points)
    return points

def getDistance(p1, p2):
    distance = math.sqrt(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2))
    return distance

def main():
    points = generateRandomPoints(10)

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (i == 0 and j ==1):
                shortestDistance = getDistance(points[i], points[j])
                p1 = points[i]
                p2 = points[j]
            else :
                if (getDistance(points[i], points[j]) < shortestDistance):
                   shortestDistance = getDistance(points[i], points[j])
                   p1 = points[i]
                   p2 = points[j] 
                

    print("The shortest distance is", shortestDistance )
    print("P1:", p1)
    print("P2: ", p2)

main()