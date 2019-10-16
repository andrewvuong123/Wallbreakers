class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # General Idea: Can just sort the lists of string s and t and check if they equal.
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        return "".join(s_list) == "".join(t_list)                