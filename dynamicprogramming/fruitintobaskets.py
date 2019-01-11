import collections
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        left, right = 0, 0
        res = 0
        cnt = collections.defaultdict(int)
        while right < len(tree):
            cnt[tree[right]] += 1
            while len(cnt) > 2:
                cnt[tree[left]] -= 1
                if cnt[tree[left]] == 0:
                    del cnt[tree[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
                
        

a = Solution()
a.totalFruit([1,2,1,0])