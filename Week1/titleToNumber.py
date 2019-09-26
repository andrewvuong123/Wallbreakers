class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # General Idea: Store values for alphabet in a dictionary, then can calculate the result from doing letter_value * 26**(len - index - 1) for every letter.
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        value = {}
        result = 0
        for i, letter in enumerate(alphabet):
            value[letter] = i + 1
            
        for i, letter in enumerate(s):
            result = result + value[letter] * 26**(len(s) - i - 1)
        return result
            
        