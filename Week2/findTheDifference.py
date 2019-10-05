from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # General Idea: Create a counter from data in s and then iterate through letters in t to find the one with count 0 from counter.
        
        a = Counter(s)
        b = Counter(t)
        for letter in t:
            if b[letter] == 0 or a[letter] != b[letter]:
                return letter
            