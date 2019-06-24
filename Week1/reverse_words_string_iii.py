class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s = s.split(" ")
        for word in s:
            char = list(word)
            char.reverse()
            result.append("".join(char))
        return " ".join(result)    