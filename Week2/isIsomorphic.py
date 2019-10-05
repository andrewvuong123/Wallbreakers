class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # General Idea: Keep a dictionary and map the letters in s as keys to the letters in t as values. If the character in s occurs again then the key exists in the dictionary and we check if the letter in t at the corresponding index equals the dict value and return false if it does not. Also check to see if any two characters in t maps to the same character.
        
        iso = {}
        for i, letter in enumerate(s):
            if letter in iso:
                if iso[letter] != t[i]:
                    return False
            elif t[i] in iso.values():
                return False
            else:
                iso[letter] = t[i]
        return True