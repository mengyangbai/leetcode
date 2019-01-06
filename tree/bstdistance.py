def allleft(values, k):
    path = []
    for i in range(1,len(values)):
        if values[i] < values[0]:
            path.append(values[i])
            
    return path

def allright(values, k):
    path = []
    for i in range(1,len(values)):
        if values[i] > values[0]:
            path.append(values[i])
            
    return path
        
        

def pathToNode(values, path, k):
    if not values or not k in values:
        return
    
    path.append(values[0])
    
    if values[0] == k:
        return
    
    if k > values[0]:
        values = allright(values,k)
        pathToNode(values,path,k)
    
    if k < values[0]:
        values = allleft(values,k)
        pathToNode(values,path,k)
    
    return
    

def bstDistance(values, n, node1, node2): 
    # WRITE YOUR CODE HERE
    if not values:
        return -1
    
    path1 = []
    pathToNode(values,path1,node1)
    path2 = []
    pathToNode(values,path2,node2)
    
    i = 0
    
    if not path1 or not path2:
        return -1
    
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i = i + 1
        
    return (len(path1) + len(path2) - 2 * i)


print(bstDistance([5,12,9,1,2,4],6,1,3))