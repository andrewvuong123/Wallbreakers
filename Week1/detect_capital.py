class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        char = list(word)
        length = len(char)
        first = 0
        up = 0
        low = 0
        for letter in char:
            if letter.isupper() and char.index(letter) == 0:
                first += 1
            if letter.isupper():
                up += 1
            if letter.islower():
                low += 1
        if up == length or low == length or (first == 1 and low == length - 1):
            return True
        else:
            return False