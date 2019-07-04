class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Idea: Create a dictionary and map letters of s as keys to letters of t as values. After the dictionary has been initialized, reiterate through s and check that the value of the initialized dictionary equals the letter at the corresponding index of t.  Do the same process vice versa with a t dictionary checking to s letters for edge cases.
        
        s_dict, t_dict = {}, {}
        for i, letter in enumerate(s):
            s_dict[letter] = t[i]
        for i, letter in enumerate(t):
            t_dict[letter] = s[i]
        
        for i, letter in enumerate(s):
            if s_dict[letter] != t[i]:
                return False
        for i, letter in enumerate(t):
            if t_dict[letter] != s[i]:
                return False
            
        return True