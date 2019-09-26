class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
       # Iterate through string and check using isupper Python function for the cases
        capital = 0
        for letter in word:
            if word.isupper() or word.islower():
                return True
            if letter.isupper():
                capital += 1
        if capital == 1 and word[0].isupper():
            return True
        if capital != len(word):
            return False
            