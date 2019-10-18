class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # General Idea: Can use the recursive edit distance algorithm to solve.
        
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        if n == 0:
            return m
        
        if word1[m-1] == word2[n-1]:
            diff = 0
        else:
            diff = 1
        
        return min(1 + self.minDistance(word1[:-1], word2), 1 + self.minDistance(word1, word2[:-1]), diff + self.minDistance(word1[:-1], word2[:-1]))
        
            
            