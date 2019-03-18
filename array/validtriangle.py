import itertools
import bisect
class BestSolution(object):
    def triangleNumber(self, g):
        g.sort()
        i = len(g)-1 
        ans = 0
        while i>1 :
            left = 0 
            right = i - 1
            while left < right:
                if g[left] + g[right] > g[i]:
                    k = bisect.bisect(g, g[i] - g[left])
                    ans += (right + k - left * 2) * (right-k+1) / 2
                    right = k-1
                else:
                    left = bisect.bisect(g, g[i] - g[right]) 
            i -= 1
        return ans

class Solution:
    def triangleNumber(self, nums: [int]) -> int:
        res = []
        for a,b,c in itertools.combinations(nums,3):
            if a + b > c and a < b + c and b < a + c and a and b and c:
                res.append([a,b,c])
        
        return res

'''
class Solution {
    public int triangleNumber(int[] nums) {
        int count = 0, N = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < N - 2; i ++) {
            for (int j = i + 1; j < N - 1; j ++) {
                int k = search(nums, j + 1, nums[i] + nums[j]);
                // sum up the possible case
                count += (k == -1 ? N - j - 1 : k - j - 1);
            }
        }
        return count;
    }
    
    private int search(int[] nums, int start, int target) {
        int low = start, hi = nums.length - 1;
        while (low <= hi) {
            int mid = low + (hi - low) / 2;
            if ( nums[mid] >= target) {
                if (low == hi) return low;
                hi = mid;
            } else {
                low = mid + 1;
            }
        }
        // all elements after start is smaller than the target
        return -1;
    }
}
'''




a = Solution()
print(a.triangleNumber([24,3,82,22,35,84,19]))