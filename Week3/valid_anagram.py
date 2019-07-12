class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Idea: Convert s and t into lists and sort then check if they equal each other.
        s, t = list(s), list(t)
        if len(s) != len(t):
            return False
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
                
            
            