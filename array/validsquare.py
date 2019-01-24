import collections
class BestSolution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d1=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        d2=(p2[0]-p3[0])**2+(p2[1]-p3[1])**2
        d3=(p3[0]-p4[0])**2+(p3[1]-p4[1])**2
        d4=(p1[0]-p4[0])**2+(p1[1]-p4[1])**2
        d5=(p1[0]-p3[0])**2+(p1[1]-p3[1])**2
        d6=(p2[0]-p4[0])**2+(p2[1]-p4[1])**2                            
        a=sorted([d1,d2,d3,d4,d5,d6])
        if max(a)==0:
            return False
        
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[4]==a[5] and a[4]==2*a[0]:
            return True
        return False

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def getDistance(p1,p2):
            return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2

        points = [p1,p2,p3,p4]
        stack = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                stack.append(getDistance(points[i],points[j]))
        
        dic = collections.Counter(stack)

        return len(dic) == 2 and 2 in dic.values() and 2 in dic.values()
