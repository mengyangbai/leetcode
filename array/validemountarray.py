class BestSolution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i, j = 0, len(A) - 1
        if j - i <2:
            return False
        while i < j and A[i] < A[i+1]:
            i += 1
        while i< j and A[j] < A[j-1]:
            j -= 1
        if i != j or i==0 or j==len(A)-1:
            return False
        return True

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) <= 2:
            return False        
        
        if not A[1] > A[0]:
            return False


        flag = True
        i = 1

        while i < len(A) and flag:
            if A[i] == A[i-1]:
                return False
            elif A[i] > A[i-1]:
                i+=1
            else:
                flag = False
        
        if i == len(A):
            return False
        
        while i < len(A):
            if A[i] < A[i-1]:
                i+=1
            else:
                return False
            
        return True

A= BestSolution()

print(A.validMountainArray([1,3,2]))

'''
class Solution {
    public boolean validMountainArray(int[] A) {
        int i = 0, j = A.length - 1;
        if(j - i <2){
            return false;
        }
        while(i < j && A[i] < A[i+1]){
            
            i += 1;
        }
        while(i< j && A[j] < A[j-1]){
            
            j -= 1;
        }
        if (i != j || i==0 || j==A.length-1){
            return false;
        }
        return true;
        
        
    }
}
'''