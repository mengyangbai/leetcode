class Solution:
    def missingElement(self, nums: [int], k: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<r:
            mid=(l+r+1)/2
            if nums[mid]-nums[0]-mid>=k:#not the result index,result is in left part.
                r=mid-1
            else:
                l=mid
        return k+nums[0]+l#nums[l]+(k-(nums[l]-nums[0]-l))
