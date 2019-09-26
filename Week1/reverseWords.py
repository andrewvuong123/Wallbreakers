class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
       # General Idea: Convert to list and point to beginning/end then swap up to the middle 
        sent = list(s)
        for i in range(0, len(sent)//2):
            start = sent[i]
            end = sent[-i-1]
            sent[i] = end
            sent[-i-1] = start
        result = "".join(sent)
        result = result.split() # split the reversed result and reverse that list to get back the initial word order
        result.reverse()
        return " ".join(result)