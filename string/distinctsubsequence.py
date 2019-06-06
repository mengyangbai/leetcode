from collections import defaultdict

class Solution:
    
    def numDistinct(self, s: str, t: str) -> int:

        # To begin, we build up an index for t that allows
        # us to quickly access all of the locations of a 
        # particular character.
        index_for_t = defaultdict(list)
        for index, letter in enumerate(t):
            index_for_t[letter].append(index)
        
        # And now we use dynamic programming to iterate 
        # through string s, keeping track of all the 
        # partial and complete solutions we've seen.
        # I further explain the trick here below.
        dp_array = [0] * (len(t) + 1)
        dp_array[0] = 1
        for character in s:
            for index in reversed(index_for_t[character]):
                dp_array[index + 1] += dp_array[index]
        
        # The solution will now be in the final dp array slot.
        return dp_array[-1]