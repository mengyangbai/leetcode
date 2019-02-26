class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        res = []
        for i in range(1,n+1):
            curstr = ''
            if i % 15 == 0:
                curstr = 'FizzBuzz'
            elif i % 5 == 0:
                curstr = 'Buzz'
            elif i % 3 == 0:
                curstr = 'Fizz'
            else:
                curstr = str(i)
            res.append(curstr)

        return res

class BestSolution:
    def fizzBuzz(self, n: 'int') -> '[str]':
        
        listy = []
        for i in range(1,n+1):
            if(i%15==0):
                listy.append("FizzBuzz")

            elif(i%5==0):
                listy.append("Buzz")

            elif(i%3==0):
                listy.append("Fizz")
            else:
                listy.append(str(i))

        return listy

a = Solution()
print(a.fizzBuzz(15))