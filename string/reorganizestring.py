import collections
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt = collections.Counter(S)
        ans = '#'
        while cnt:
            stop = True
            for v,_ in cnt.most_common():
                if v != ans[-1]:
                    stop = False
                    ans += v
                    cnt[v] -= 1
                    if not cnt[v]:
                        del cnt[v]
                    
                    break
            
            if stop:
                break
        return ans[1:] if len(ans) == len(S)+1 else ''
        

a = Solution()
print(a.reorganizeString("baa"))
        