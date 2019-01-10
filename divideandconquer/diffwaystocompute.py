class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        def helper(op,left,right):
            if op == '+':
                return left + right
            if op == '-':
                return left - right
            if op == '*':
                return left * right

        res = []
        if input.isdigit():
            return [int(input)]

        for e,v in enumerate(input):
            if v in "+-*":
                [left] = self.diffWaysToCompute(input[:e])
                [right] = self.diffWaysToCompute(input[e+1:])
                res.append(helper(v,left,right))
                
        return res