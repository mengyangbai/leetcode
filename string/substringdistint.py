def isDistinct(s):
    if len(s) == len(set(s)):
        return True
    return False
    
def subStringsKDist(inputStr, num):
    # WRITE YOUR CODE HERE
    if not inputStr or len(inputStr) < num:
        return []
    
    n = len(inputStr)
    
    res = []
    for i in range(len(inputStr)):
        if i + num <= n:
            tmpstr = inputStr[i:i+num]
            if isDistinct(tmpstr) and tmpstr not in res:
                res.append(tmpstr)
                
    return res

subStringsKDist("abcd",3)