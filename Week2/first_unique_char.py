from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Idea: Create a counter from the given string to get count of each digit. Iterate through each letter in the string and return the index of the first letter with a count of 1. Else return -1 if no non-repeating letter exists.
        
        c = Counter(s)
        for index, letter in enumerate(s):
            if c[letter] == 1:
                return index
        return -1