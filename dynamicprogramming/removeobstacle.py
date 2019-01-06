def removeObstacle(numRows,numColumns,lot):
    def helper(lot,dp,x,y):
        x1 = x + 1
        x2 = x - 1
        y1 = y + 1
        y2 = y - 1


        if x1 >= 0 and x1 < numRows and y >= 0 and y < numColumns:
            if lot[x1][y]  == 0:
                dp[x1][y] = -1
            else:
                if dp[x1][y] > dp[x][y]:
                    dp[x1][y] = min(dp[x1][y],dp[x][y] + 1)
                    helper(lot,dp,x1,y)
        
        if x2 >= 0 and x2 < numRows and y >= 0 and y < numColumns:
            if lot[x2][y]  == 0:
                dp[x2][y] = -1
            else:
                if dp[x2][y] > dp[x][y]:
                    dp[x2][y] = min(dp[x2][y],dp[x][y] + 1)
                    helper(lot,dp,x2,y) 
        
        if x >= 0 and x < numRows and y1 >= 0 and y1 < numColumns:
            if lot[x][y1]  == 0:
                dp[x][y1] = -1
            else:
                if dp[x][y1] > dp[x][y]:
                    dp[x][y1] = min(dp[x][y1],dp[x][y] + 1)
                    helper(lot,dp,x,y1)
        
        if x >= 0 and x < numRows and y2 >= 0 and y2 < numColumns:
            if lot[x][y2]  == 0:
                dp[x][y2] = -1
            else:
                if dp[x][y2] > dp[x][y]:
                    dp[x][y2] = min(dp[x][y2],dp[x][y] + 1)
                    helper(lot,dp,x,y2)     


    dp = [[999999 for _ in range(numRows) ] for _ in range(numColumns)]
    if lot[0][0] == 0:
        return -1
    
    dp[0][0] = 0

    helper(lot,dp, 0, 0)

    for i in  range(numRows):
        for j in range(numColumns):
            if lot[i][j] == 9:
                if dp[i][j] == 999999:
                    return -1
                return dp[i][j]


print(removeObstacle(3,3,[[1,0,0],[1,0,1],[1,9,1]]))