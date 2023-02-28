import math
import random

def getDistancePoints(point1, point2, ctrOpt):
    dist = 0
    for i in range (len(point1)):
        dist += (point1[i] - point2[i]) ** 2

    ctrOpt+=1;
    return math.sqrt(dist), ctrOpt

def appendIfNotSame(closestPairs, pointPair):
    has_common_element = False
    for arr in closestPairs:
        if (pointPair == [[]]):
            has_common_element = True
            break
        if ((pointPair[0] == arr[0] or pointPair[0] == arr[1]) and (pointPair[1] == arr[0] or pointPair[1] == arr[1])):
            has_common_element = True
            break

    # Melakukan append hanya jika pasangan point pada pointPair tidak sama dengan salah satu pasangan pada closestPairs
    if not has_common_element:
        closestPairs.append(pointPair)
    return closestPairs

def extendIfNotSame(closestPairs, pointPairs):
    for arr in pointPairs:
        closestPairs = appendIfNotSame(closestPairs, arr)

    return closestPairs

def formatPoint(point):
    strPoint = "("
    i = 0
    while (i < len(point)-1):
        strPoint = strPoint + str(point[i]) + " , " 
        i += 1
        
    strPoint = strPoint + str(point[i]) + ")"

    return strPoint

def generateRandomPoints(total_points, total_dim) :
    points = [[0 for j in range (total_dim)] for i in range(total_points)]

    for i in range (total_points) :
        for j in range (total_dim) :
            points[i][j] = round(random.uniform(-100, 100),2)
    
    print(points)
    return points