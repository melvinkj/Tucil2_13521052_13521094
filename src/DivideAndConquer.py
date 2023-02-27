import numpy as np
from BruteForce import bruteForce
from Utils import getDistancePoints, appendIfNotSame, extendIfNotSame 

# TODO: ask if ada wajib pake sorting dgn metode apa
# Points is an array of points, index specify the index of coordinates to be sorted on
def quickSortPoints(points, index):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        left = []
        right = []
        for point in points[1:]:
            if point[index] < pivot[index]:
                left.append(point)
            else:
                right.append(point)
        return quickSortPoints(left, index) + [pivot] + quickSortPoints(right, index)

# Points is an array of points which already sorted (asc) based on x coordinate
def dividePoints(points: np.array):
    midIdx = points.shape[0] // 2
    if (points.shape[0] % 2 == 0):
        return (points[midIdx-1, 0] + points[midIdx, 0]) / 2, points[0:midIdx+1], points[midIdx:]
    else:
        return points[midIdx, 0],points[0:midIdx + 1], points[midIdx: ]
    
# def bruteForce(points):
#     closestPairs = []
#     for i in range(len(points)):
#         for j in range(i+1, len(points)):
#             if (i == 0 and j ==1):
#                 shortestDistance = getDistancePoints(points[i], points[j])
#                 closestPair = [points[i], points[j]]
#                 closestPairs.append(closestPair)
#             else :
#                 if (getDistancePoints(points[i], points[j]) < shortestDistance):
#                    shortestDistance = getDistancePoints(points[i], points[j])
#                    closestPairs = []
#                    closestPair = [points[i], points[j]]
#                    closestPairs.append(closestPair)
#                 elif (getDistancePoints(points[i], points[j]) == shortestDistance):
#                    closestPair = [points[i], points[j]]
#                    closestPairs = appendIfNotSame(closestPairs, closestPair)
#     return closestPairs, shortestDistance

def findStripClosest(points, dist, dim):
    closestDist = dist
    if (dim <= 2):
        newStripPoints = points
        closestPairs = []
        if (dim == 2):
            newStripPoints = quickSortPoints(points, dim - 1)
        n = len(newStripPoints)
        for i in range (n):
            for j in range (i+1, n):
                if (abs(newStripPoints[i][dim-1] - newStripPoints[j][dim-1]) > closestDist):
                    break
                if (getDistancePoints(newStripPoints[i], newStripPoints[j]) < closestDist):
                    closestPairs = []
                    closestDist = getDistancePoints(newStripPoints[i], newStripPoints[j])
                    closestPair = [newStripPoints[i], newStripPoints[j]]
                    closestPairs = [closestPair]
                elif (getDistancePoints(newStripPoints[i], newStripPoints[j]) == closestDist):
                    closestPair = [newStripPoints[i], newStripPoints[j]]
                    closestPairs = appendIfNotSame(closestPairs, closestPair)
    else:
        closestPairs, closestDist = findClosestPair(points, len(points), dim-1)
    return closestPairs, closestDist



def findClosestPair(unsortedPoints, n: int, dim: int):
    if (n == 2):
        closestPair = unsortedPoints
        closestPairs = [closestPair]
        closestDist = getDistancePoints(unsortedPoints[0], unsortedPoints[1])
    elif (n == 3):
        closestPairs, closestDist = bruteForce(unsortedPoints)
    else:
        # midPoint, leftPartPoints, rightPartPoints = dividePoints(points)
        # print(midPoint, leftPartPoints, rightPartPoints)
        points = quickSortPoints(unsortedPoints, len(unsortedPoints[0]) - dim)
        # print(points)
        mid = n // 2
        midPoint = points[mid][len(unsortedPoints[0]) - dim]
        leftPart = points[0:mid]
        rightPart = points[mid:]

        # print(leftPart)
        # print(rightPart)

        leftClosestPoints, distLeftPair = findClosestPair(leftPart, len(leftPart), dim)
        rightClosestPoints, distRightPair = findClosestPair(rightPart, len(rightPart), dim)
        closestPairs = []
        # print(leftClosestPoints)
        # print(rightClosestPoints)
        # print(closestPairs)

        # TODO: consider if there are two pair with the same distance?
        if (distLeftPair < distRightPair):
            closestPairs = leftClosestPoints
            closestDist = distLeftPair
        elif (distRightPair < distLeftPair):
            closestPairs = rightClosestPoints
            closestDist = distRightPair
        elif (distRightPair == distLeftPair):
            closestPairs = leftClosestPoints
            closestPairs = extendIfNotSame(closestPairs, rightClosestPoints)
            closestDist = distLeftPair
        # print("closest from halfves: ", closestPairs, closestDist)
        leftBound = midPoint - closestDist
        rightBound = midPoint + closestDist

        # closestDist adalah delta untuk mencari di sekitar garis pembagi
        filteredPoints = [x for x in points if leftBound <= x[len(unsortedPoints[0]) - dim] <= rightBound]
        stripClosestPoints, distStripPair = findStripClosest(filteredPoints, closestDist, dim)
        # print(stripClosestPoints)
        # print("points in strip: ", filteredPoints)
        # print("closest points in strip", stripClosestPoints,distStripPair)
        # print("current dimension", dim)
        # print()

        if (distStripPair < closestDist):
            closestPairs = []
            closestPairs = stripClosestPoints
            closestDist = distStripPair
        elif (distStripPair == closestDist):
            closestPairs = extendIfNotSame(closestPairs, stripClosestPoints)
        # print(stripClosestPoints)
        # print(closestPairs)
        
    return closestPairs, closestDist
        
                    




if __name__=="__main__":
    # Function testing
    test = [[2, 6, 1, 4], [5, 4, 3, 1], [1, 3, 5, 6], [15, 4, 1, 7], [5, 6, 7, 8], [3, 4, 5, 1]]
    print(findClosestPair(test, 6, 4))