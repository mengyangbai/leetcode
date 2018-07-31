class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):

        l1 = len(num1)
        sum=0
        for index in range(l1):
            if index != l1-1:
                sum = sum + (int(num1[index]) * int(num2) * 10**(l1-1-index))
            else:
                sum = sum + (int(num1[index]) * int(num2) )
        return str(sum)
