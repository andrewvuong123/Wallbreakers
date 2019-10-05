from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # General Idea: Create a counter with data from paragraph and then iterate the elements of counter and check which one is the greatest that is also not in banned. Also have to convert paragraph string into lowercase list of words without punctuation.
        
        for p in "!?',;.":
            paragraph = paragraph.replace(p, " ") 
        words = paragraph.lower() 
        words = words.split() 
        c = Counter(words)
        result = 0
        for word, coun in c.most_common():
            if word not in banned:
                return word
        return ""