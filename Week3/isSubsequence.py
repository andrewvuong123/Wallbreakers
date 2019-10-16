class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # General Idea: Keep pointers to s and t and increment s when s and t matches. If s_p reaches end of s then return true else false.
        
        s_p = 0
        t_p = 0
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1
        return s_p == len(s)