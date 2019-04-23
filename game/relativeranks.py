import heapq

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return None
        
        # build a max heap O(n) time in place
        rankHeap = [-x for x in nums]
        heapq.heapify(rankHeap)
        
        # build map of ranks
        rankMap = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(nums)):
            if i <= 2:
                rank = -1 * heapq.heappop(rankHeap)
                rankMap[rank] = medals[i]
            else:
                rank = -1 * heapq.heappop(rankHeap)
                rankMap[rank] = str(i+1)
                
        return [rankMap[rank] for rank in nums]
        
'''
    String[] base = {"Gold Medal","Silver Medal","Bronze Medal"};
    String[] re = new String[nums.length];
    int[] copy = Arrays.copyOf(nums,nums.length);
    Map<Integer,Integer> map = new HashMap<>();
    Arrays.sort(copy);
    for (int i = 0; i < nums.length; i++) {
        map.put(copy[i],nums.length - 1 - i);
    }

    int rank = 0;
    for (int i = 0; i < nums.length; i++) {
        rank = map.get(nums[i]);
        re[i] = rank < 3 ? base[rank] : String.valueOf(rank + 1);
    }

    return re;
'''