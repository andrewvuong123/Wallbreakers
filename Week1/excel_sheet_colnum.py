class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        sep = list(s)
        total = 0
        exp = len(sep) - 1
        for letter in sep:
            num = ord(letter) - 64
            total = num * 26**exp + total
            exp = exp - 1
        return total