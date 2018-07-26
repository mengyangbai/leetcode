class Node(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = Node()
                node.children[letter] = child
            node = child

        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        res = ''
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                break
            res += letter
            if node.isWord:
                return res

        return word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for prefix in dict:
            trie.insert(prefix)

        res = []
        for word in sentence.split():
            res.append(trie.search(word))

        return ' '.join(res)
