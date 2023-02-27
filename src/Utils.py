import math

def getDistancePoints(point1, point2):
    dist = 0
    for i in range (len(point1)):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)

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