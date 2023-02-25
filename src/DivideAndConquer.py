import numpy as np
import Utils

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
    
def findClosestPair(points: np.array, n: int):
    print(points)
    if (n == 2):
        closestPair = points
        closestDist = Utils.getDistancePoints(points[0], points[1])
        return closestPair, closestDist
    # elif (n == 3):
    #     closestDist = Utils.getDistancePoints(points[0], points[1])
    #     for i in range (3):
    #         for j in range (i+1, 3):
    #             dist = Utils.getDistancePoints(points[i], points[j])
    #             if (dist < closestDist):
    #                 closestDist = dist
    #                 closestPair = np.array(points[i], points[j])
    else:
        midPoint, leftPartPoints, rightPartPoints = dividePoints(points)
        print(midPoint, leftPartPoints, rightPartPoints)

        # mid = n //2
        # midPoint = points[mid]
        # leftPartPoints = points[0:mid]
        # rightPartPoints = points[mid:]

        leftClosestPoints, distLeftPair = findClosestPair(leftPartPoints, leftPartPoints.shape[0])
        rightClosestPoints, distRightPair = findClosestPair(rightPartPoints, rightPartPoints.shape[0])

        # TODO: consider if there are two pair with the same distance?
        closestPair = leftClosestPoints if distLeftPair <= distRightPair else rightClosestPoints
        closestDist = distLeftPair if distLeftPair <= distRightPair else distRightPair

        # closestDist adalah delta untuk mencari di sekitar garis pembagi
        filteredPoints = points[np.where((points[:,0] >= midPoint - closestDist) & (points[:,0] <= midPoint + closestDist))]
        newStripPoints = np.array(quickSortPoints(filteredPoints, 1))
        pointsDist = np.empty(newStripPoints.shape[1])

        for i in range (newStripPoints.shape[0]):
            for j in range (i+1, newStripPoints.shape[0]):
                for k in range (newStripPoints.shape[1]):
                    pointsDist[k] = abs(newStripPoints[i, k] - newStripPoints[j, k])
                if np.all(pointsDist <= closestDist):
                    newDist = Utils.getDistancePoints(newStripPoints[i], newStripPoints[j])
                    if newDist < closestDist:
                        closestDist = newDist
                        closestPair = np.array([newStripPoints[i], newStripPoints[j]])
        
        return closestPair, closestDist
        
                    




if __name__=="__main__":
    # Function testing
    test = [[2, 1, 4], [2, 3, 4], [1, -9, 4], [2, 15, 4], [-2, 1, 4], [5, -16, 4]]
    arrlsit = quickSortPoints(test, 0)
    arr = np.array(arrlsit)
    print(findClosestPair(arr, 6))