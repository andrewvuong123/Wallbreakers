from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # General Idea: Set a counter for letters in s, then iterate through based on most common. While the count is greater than one append that letter to a list and decrement the count.
        
        c = Counter(s)
        result = []
        for letter, count in c.most_common():
            while count >= 1:
                result.append(letter)
                count -= 1
        return "".join(result)
            
        
        