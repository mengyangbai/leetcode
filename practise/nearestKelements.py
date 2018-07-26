def search(self, reader, target):
    index, exp = 0, 0
    while True:
        if reader.get(index) == target:
            return index
        elif reader.get(index) < target:
            index = 2**exp
            exp += 1
        else:
            break
    left = (index/2) + 1
    right = index - 1
    while left <= right:
        mid = left+(right-left)//2
        if reader.get(mid) == target:
            return mid
        elif reader.get(mid) < target:
            left = mid+1
        else:
            right = mid-1
    return -1
