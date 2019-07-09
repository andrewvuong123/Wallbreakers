class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Idea: Keep pointers to both strings and increment letter s when t points to the same letter. If reach the end of s return true, else return false
        
        count = 0
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                count += 1
                s_index += 1
                t_index += 1
            else:
                t_index += 1
        return count == len(s)
        