class Solution:
    def trap(self, height: [int]) -> int:
        if not height:
            return 0
        
        left,right = 0,len(height)-1
        res = 0
        maxleft,maxright = 0, 0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]

                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                
                right -= 1

        return res