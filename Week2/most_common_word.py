from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Idea: Use lower function to convert words to lower case in paragraph string and split words into a list. Use counter to get count of each word in list. Iterate through counter using most common function and find the most common word not in banned.
        # Get rid of punctuation
        for p in "!?',;.":
            paragraph = paragraph.replace(p, " ") # Replace with space in case comma removal causes concatenation of letters
                
        words = paragraph.lower() # lower
        words = words.split() # split
        c = Counter(words)
        for word, count in c.most_common():
            if word not in banned:
                return word
        return ""