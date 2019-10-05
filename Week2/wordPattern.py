class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # General Idea: Map each letter in the pattern to the word value in the string in a dictionary. Check for three cases, if the letter is in the dictionary then check if its value matches the str word. Also check if words in str map to more than one letter. Else add the key value pair to the dictionary.
        
        words = str.split(" ") #split up words in str
        if len(pattern) != len(words):
            return False
        match = {}
        for i, letter in enumerate(pattern):
            if letter in match:
                if match[letter] != words[i]:
                    return False
            elif words[i] in match.values():
                return False
            else:
                match[letter] = words[i]
        return True