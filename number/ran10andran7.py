def rand7():
    pass

class Solution:
    def rand10(self):
        c = rand7() * 7 + rand7() - 8
        if c < 40:
            return (c % 10) + 1
						
        # Here c ~ [40..48]
        # Thus (c % 10) ~ [0..8]
        # Thus e ~ [0..62]
        e = (c % 10)*7 + rand7() - 1 
        if e < 60:
            return (e % 10) + 1
						
        return self.rand10()