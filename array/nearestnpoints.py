def ClosestXdestinations(numDestinations, allLocations, numDeliveries):
    dic={}

    if not allLocations:
        return []

    for point in allLocations:
        value = point[0]*point[0]+point[1]* point[1]
        if tuple(point) in dic:
            dic[tuple(point)][1] += 1
        else:
            dic[tuple(point)] = [value,1]

    res = []
    n = 0

    for key in sorted(dic, key=dic.__getitem__):
        if n < numDeliveries:
            for _ in range(dic[key][1]):
                res.append(list(key))
                n+=1
        else:
            break

    return res

print(ClosestXdestinations(6,[[1,2],[1,2],[5,3],[2,7],[1,8],[7,9]],3))