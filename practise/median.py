class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        idx = []

        if (len(nums1) + len(nums2)) % 2 == 0:
            idx.append((len(nums1) + len(nums2)) >> 1)
            idx.append(((len(nums1) + len(nums2)) >> 1) - 1)
        else:
            idx.append((len(nums1) + len(nums2)) >> 1)

        nums3 = sorted(nums1 + nums2)
        if len(idx) == 2:
            return (nums3[idx[0]] + nums3[idx[1]]) / 2.0
        else:
            return nums3[idx[0]] * 1.0


a = []
b = [1, 2, 3, 4, 5, 6]
s = Solution()
print(s.findMedianSortedArrays(a, b))
