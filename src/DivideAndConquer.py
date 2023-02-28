from BruteForce import bruteForce
from Utils import getDistancePoints, appendIfNotSame, extendIfNotSame 

# Quicksort function to sort points based on index
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

# Recursive function to find closest pair of points in the stripe with dim dimensions
def findStripClosest(points, dist, dim, ctr):
    # Initialize closest distance
    closestDist = dist
    # Compute the closest dist only if the dimension is 2
    if (dim <= 2):

        if(len(points) <= 1):
            return None, None, ctr

        newStripPoints = points
        closestPairs = []
        if (dim == 2):
            newStripPoints = quickSortPoints(points, dim - 1)
        n = len(newStripPoints)
        for i in range (n):
            for j in range (i+1, n):
                if (abs(newStripPoints[i][dim-1] - newStripPoints[j][dim-1]) > closestDist):
                    break
                distPoint, ctr = getDistancePoints(newStripPoints[i], newStripPoints[j], ctr)
                if (distPoint < closestDist):
                    closestPairs = []
                    closestDist = distPoint
                    closestPair = [newStripPoints[i], newStripPoints[j]]
                    closestPairs = [closestPair]
                elif (distPoint == closestDist):
                    closestPair = [newStripPoints[i], newStripPoints[j]]
                    closestPairs = appendIfNotSame(closestPairs, closestPair)
    # If the dimension is not two
    else:
        closestPairs, closestDist, ctr = findClosestPair(points, len(points), dim-1, ctr)
    return closestPairs, closestDist, ctr



def findClosestPair(unsortedPoints, n: int, dim: int, ctr: int):
    # if (n == 2):
    #     closestPairs = [unsortedPoints]
    #     closestDist, ctr = getDistancePoints(unsortedPoints[0], unsortedPoints[1], ctr)
    #     print("hyhy ini brute force",unsortedPoints)
    # elif (n == 3):
    #     print("ini brute force 3")
    #     closestPairs, closestDist, ctr = bruteForce(unsortedPoints, ctr)
    if (n <= 3):
        closestPairs, closestDist, ctr = bruteForce(unsortedPoints, ctr)
    else:
        # midPoint, leftPartPoints, rightPartPoints = dividePoints(points)
        # print(midPoint, leftPartPoints, rightPartPoints)
        print(unsortedPoints)
        print()
        points = quickSortPoints(unsortedPoints, len(unsortedPoints[0]) - dim)
        # print(points)
        mid = n // 2
        midPoint = points[mid][len(unsortedPoints[0]) - dim]
        leftPart = points[0:mid]
        rightPart = points[mid:]
        print("Two Halves:")

        print(leftPart, len(leftPart))
        print(rightPart, len(rightPart))
        print()

        leftClosestPoints, distLeftPair, ctr = findClosestPair(leftPart, len(leftPart), dim, ctr)
        rightClosestPoints, distRightPair, ctr = findClosestPair(rightPart, len(rightPart), dim, ctr)
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
        else:
            closestPairs = leftClosestPoints
            closestPairs = extendIfNotSame(closestPairs, rightClosestPoints)
            closestDist = distLeftPair
        # print("closest from halfves: ", closestPairs, closestDist)
        leftBound = midPoint - closestDist
        rightBound = midPoint + closestDist

        # closestDist adalah delta untuk mencari di sekitar garis pembagi
        filteredPoints = [x for x in points if leftBound <= x[len(unsortedPoints[0]) - dim] <= rightBound]
        stripClosestPoints, distStripPair, ctr = findStripClosest(filteredPoints, closestDist, dim, ctr)
        # print(stripClosestPoints)
        # print("points in strip: ", filteredPoints)
        # print("closest points in strip", stripClosestPoints,distStripPair)
        # print("current dimension", dim)
        # print()

        if (stripClosestPoints != None):
            if (distStripPair < closestDist):
                closestPairs = []
                closestPairs = stripClosestPoints
                closestDist = distStripPair
            elif (distStripPair == closestDist):
                closestPairs = extendIfNotSame(closestPairs, stripClosestPoints)
        # print(stripClosestPoints)
        # print(closestPairs)
        
    return closestPairs, closestDist, ctr
        
                    




if __name__=="__main__":
    # Function testing
    test = [[53, 69, 54], [69, 38, -7], [-83, -34, 96], [-3, 95, 72], [-3, -85, 68], [-91, 58, 31], [92, 10, -78], [-41, 87, 53]]
    print(findClosestPair(test, 8, 3, 0))