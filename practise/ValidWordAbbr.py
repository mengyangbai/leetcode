class ValidWordAbbr(object):
    def abbreviation(self, word):
        return word[0] + str(len(word) - 2) + word[-1] if word > 2 else word

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = {}
        for d in dictionary:
            abb = self.abbreviation(d)
            if abb in self.dic:
                self.dic[abb] = ""
            else:
                self.dic[abb] = d

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abb = self.abbreviation(word)

        if self.dic[abb] == "":
            return False
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
