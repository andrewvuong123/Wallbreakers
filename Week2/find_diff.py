from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Idea: Keep a counter for s and t and iterate through t to find the letter with a count of zero or the letter whose count does not match between s and t.
        
        s_count, t_count = Counter(s), Counter(t)
        
        for letter in t:
            if t_count[letter] == 0 or t_count[letter] != s_count[letter]:
                return letter