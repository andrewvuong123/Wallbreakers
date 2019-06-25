class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram = {}
        if len(s) != len(t):
            return False
        for letter in s: #initializing dictionary
            if letter in anagram:
                anagram[letter] += 1
            else:
                anagram[letter] = 1
    
        for letter in t: #checking letters
            if letter in anagram:
                anagram[letter] -= 1
            if letter not in anagram or anagram[letter] < 0:
                return False
        return True