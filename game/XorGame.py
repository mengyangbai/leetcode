class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        42ms
        """
        start = 0
        # 一开始就赢了
        for num in nums:
            start ^= num
        if start == 0:
            return True
        else:
        # 否则A要赢只有在A取走一个值之后，给B剩下的奇数个相同的数，此时B没有别的方法，不然B不会被将死
        # 所以到B的时候一定为奇数个数。如果在奇数个数的B没被将死，则A不可能被将死，同上。所以游戏能继续到B只剩一个数或被将死
            if len(nums) % 2 == 0:
                return True
            else:
                return False