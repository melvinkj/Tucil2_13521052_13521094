import math

def getDistancePoints(point1, point2):
    dist = 0
    for i in range (len(point1)):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)

