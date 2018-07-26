dic = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def dfs(num, allstr, res):
            if num == length:
                res.append(allstr)
                return

            for letter in dic[digits[num]]:
                dfs(num + 1, allstr + letter, res)

        length = len(digits)
        res = []

        dfs(0, '', res)

        return res
