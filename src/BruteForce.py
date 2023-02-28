import Utils

def bruteForce(points, ctr):
    if (len(points) <= 1):
        return None, None, ctr

    closestPairs = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (i == 0 and j ==1):
                shortestDistance, ctr = Utils.getDistancePoints(points[i], points[j], ctr)
                closestPairs += [[points[i], points[j]]]
            else :
                distPoint, ctr = Utils.getDistancePoints(points[i], points[j], ctr)
                if (distPoint < shortestDistance):
                    closestPairs = []
                    shortestDistance = distPoint
                    closestPairs = [[points[i], points[j]]]
                elif (distPoint == shortestDistance):
                    closestPair = [points[i], points[j]]
                    closestPairs = Utils.appendIfNotSame(closestPairs, closestPair)
    
    return closestPairs, shortestDistance, ctr 