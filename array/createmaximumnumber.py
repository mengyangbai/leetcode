class Solution:
    def maxNumber(self, nums1: [int], nums2: [int], k: int) -> [int]:
        
        def getMax(nums,t):
            ans = []
            size = len(nums)
            for x in range(size):
                while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                    ans.pop()
                if len(ans) < t:
                    ans += nums[x],

            return ans


        def merge(nums1,nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]

            return ans
        
        len1,len2 = len(nums1),len(nums2)
        res = []

        for x in range(max(0,k-len2),min(k,len1)+1):
            tmp = merge(getMax(nums1,x),getMax(nums2,k-x))
            res = max(tmp,res)

        return res


class BetterSolution:
    def maxNumber(self, nums1: [int], nums2: [int], k: int) -> [int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        
        bfs
        nums1[i:]: entries in nums1 that are still available given the choices made
        nums2[j:]: ^
        outer loop: runs k times. each time we pick a number.
        need: # entries still needed in ret
        suffix1: given i, j, and need, not all entries in nums1 are choosable, because we'd run out of entries
        suffix1: ^
        best: for every need, best is the max digit available. if it is choosable in both suffix1 and suffix2, branch the search
        """
        ret = []
        p = set([(0, 0)])
        for need in range(k, 0, -1):
            best = -1
            for i, j in p:
                suffix1 = nums1[i: len(nums1) + len(nums2) - j - need + 1]
                suffix2 = nums2[j: len(nums1) + len(nums2) - i - need + 1]
                cand = max(suffix1 + suffix2)
                if cand > best:
                    best = cand
                    q = set()
                elif cand < best:
                    continue
                if best in suffix1:
                    q.add((i + suffix1.index(best) + 1, j))
                if best in suffix2:
                    q.add((i, j + suffix2.index(best) + 1))
            p = q
            ret.append(best)
        return ret
#     def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         n, m= len(nums1),len(nums2)
#         ret = [0] * k
#         for i in range(0, k+1):
#             j = k - i
#             if i > n or j > m: continue
#             left = self.maxSingleNumber(nums1, i)
#             right = self.maxSingleNumber(nums2, j)
#             num = self.mergeMax(left, right)
#             ret = max(num, ret)
#         return ret


#     def mergeMax(self, nums1, nums2):
#         ans = []
#         while nums1 or nums2:
#             if nums1 > nums2:
#                 ans += nums1[0],
#                 nums1 = nums1[1:]
#             else:
#                 ans += nums2[0],
#                 nums2 = nums2[1:]
#         return ans

#     def maxSingleNumber(self, nums, selects):
#         n = len(nums)
#         ret = [-1]
#         if selects > n : return ret
#         while selects > 0:
#             start = ret[-1] + 1 #search start
#             end = n-selects + 1 #search end
#             ret.append( max(range(start, end), key = nums.__getitem__))
#             selects -= 1
#         ret = [nums[item] for item in ret[1:]]
#         return ret