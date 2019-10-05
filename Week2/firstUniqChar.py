from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # General Idea: Populate the counter with data from s and then iterate through the string to see which letter returns 1 for its count first, else return -1 if there isn't one.
        
        c = Counter(s)
        for i,letter in enumerate(s):
            if c[letter] == 1:
                return i
        return -1
        