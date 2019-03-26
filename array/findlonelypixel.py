class BestSolution:
    def findLonelyPixel(self, picture: [[str]]) -> int:
        r = list(zip(*picture))
        res = 0
        for row in picture:
            if row.count('B') == 1:
                index = row.index('B')
                if r[index].count('B') == 1:
                    res += 1
        return res

class MySolution:
    def findLonelyPixel(self, picture: [[str]]) -> int:
        if not picture:
            return 0

        self.res = 0


        def validlongly(i,j):
            flag = True
            for m,_ in enumerate(picture):
                if m != i and picture[m][j] == 'B':
                    flag = False
                
            for n,_ in enumerate(picture[0]):
                if n != j and picture[i][n] == 'B':
                    flag = False

            if flag:
                self.res += 1

        for i,_ in enumerate(picture):
            for j,_ in enumerate(picture[0]):
                if picture[i][j] == 'B':
                    validlongly(i,j)

        return self.res

'''
 public int findLonelyPixel(char[][] picture) {
    int n = picture.length, m = picture[0].length;
    
    int[] rowCount = new int[n], colCount = new int[m];
    for (int i=0;i<n;i++) 
        for (int j=0;j<m;j++) 
            if (picture[i][j] == 'B') { rowCount[i]++; colCount[j]++; }

    int count = 0;
    for (int i=0;i<n;i++) 
        for (int j=0;j<m;j++) 
            if (picture[i][j] == 'B' && rowCount[i] == 1 && colCount[j] == 1) count++;
                
    return count;
}
'''

a = BestSolution()
print(a.findLonelyPixel([['W', 'W', 'W'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]))

