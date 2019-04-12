class Solution:
    def numRookCaptures(self, board: [[str]]) -> int:     
        for i in range(8):
            for j in range(8):
                if 'R' == board[i][j]:
                    result = 0
                    for vector in [(1,0),(-1,0),(0,1),(-0,-1)]:
                        x,y = i,j
                        while 0 <= x + vector[0] < 8 and 0 <= y + vector[1] < 8 and board[x+vector[0]][y+vector[1]] != 'B':
                            x = x + vector[0]
                            y = y + vector[1]
                            if board[x][y] == 'p':
                                result += 1
                                break
                    return result        
        return 0

a = Solution()
print(a.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))

'''
class Solution {
    public int numRookCaptures(char[][] board) {
        
        int x=0;
        int y=0;
        int count = 0;
        
        for(int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                if (board[i][j]=='R') {
                    x = i;
                    y = j;
                }
            }
        }
        
        int xt = x-1;
        
        while (xt>=0 && board[xt][y]=='.') {
            xt--;
        }
        if (xt>-1 && board[xt][y]=='p') {
            count++;
        }
        
        xt = x+1;
        
        while (xt<8 && board[xt][y]=='.') {
            xt++;
        }
        if (xt<8 && board[xt][y]=='p') {
            count++;
        }
        
        int yt = y-1;
        
        while (yt>=0 && board[x][yt]=='.') {
            yt--;
        }
        if (yt>-1 && board[x][yt]=='p') {
            count++;
        }
        
        yt = y+1;
        
        while (yt<8 && board[x][yt]=='.') {
            yt++;
        }
        if (yt<8 && board[x][yt]=='p') {
            count++;
        }
        
        return count;
        
    }
}
'''