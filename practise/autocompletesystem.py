class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sentences = set()


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.buffer = ''
        self.stimes = dict()
        self.trie = TrieNode()
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.tnode = self.trie

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        ans = []
        if c != '#':
            self.buffer += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                ans = sorted(
                    self.tnode.sentences,
                    key=lambda x: (-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.trie
        return ans

    def addSentence(self, sentence):
        node = self.trie
        for letter in sentence:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
            child.sentences.add(sentence)

'''
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.hashmap = collections.defaultdict(list) # prefix: [sentence]
        self.hashmap1 = collections.defaultdict(int) # sentence: times
        
        for time, sentence in zip(times, sentences):
            self.update(sentence, time)
            
        self.inputs = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if not c == '#':
            self.inputs += c
            if not self.inputs in self.hashmap:
                return []
            sentences = self.hashmap[self.inputs]
            
            temp = []
            for sentence in sentences:
                temp.append((self.hashmap1[sentence], sentence))
                
            result = []
            temp.sort(cmp = self.compare)
            for x in temp:
                result.append(x[1])
            return result
        else:
            self.update(self.inputs, 1)
            self.inputs = ''
            return []
        
        
    def compare(self, x1, x2):
        if x1[0] > x2[0]:
            return -1
        if x1[0] < x2[0]:
            return 1
        if x1[1] < x2[1]:
            return -1
        if x1[1] > x2[1]:
            return 1
        return 0
        
        
    def deleteSentence(self, l):
        ls = collections.deque(l)
        minimum = float('inf')
        for x in ls:
            minimum = min(minimum, self.hashmap1[x])
            
        # minimum = min(self.hashmap1[x] for x in list)
        mins = []
        for i, x in enumerate(l):
            if self.hashmap1[x] == minimum:
                mins.append((i, x))
                
        target = ' '
        index = None
        for x in mins:
            if x[1] > target:
                target = x[1]
                index = x[0]
                
        ls[index], ls[-1] = ls[-1], ls[index]
        ls.pop()
        return ls
        
    def update(self, sentence, time):
        self.hashmap1[sentence] += time
            
        for i in range(len(sentence)):
            prefix = sentence[:i + 1]
            if not prefix in self.hashmap:
                self.hashmap[prefix] = [sentence]
            else:
                if not sentence in self.hashmap[prefix]:
                    self.hashmap[prefix].append(sentence)
                    if len(self.hashmap[prefix]) > 3:
                        self.hashmap[prefix] = self.deleteSentence(self.hashmap[prefix])
'''