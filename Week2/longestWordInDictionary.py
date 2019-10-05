class TrieNode(object):
     def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.end = False
        self.word = ''
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """ 
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True
        curr.word = word

    def bfs(self):
        """
        Conducts bfs search using queue
        """
        queue = collections.deque([self.root]) #create queue from root
        result = ''
        while queue:
            curr = queue.popleft() # pop element from left end of queue
            for node in curr.children.values(): # check children of current popped element
                if node.end: # if it is the end of a word then append to the queue
                    queue.append(node)
                    if len(node.word) > len(result) or node.word < result: # check if the word at the end node is greater than the length of result and update result 
                        result = i.word
        return result
    
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        t = Trie()
        for word in words:
            t.insert(word)
        return t.bfs()
        