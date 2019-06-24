class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = list(s)
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} #faster to see if obj present in a set than a list
        indices = []
        new_v = []
        for i, letter in enumerate(char):
            if letter in vowel:
                indices.append(i)
                new_v.append(letter)
        new_v.reverse()
        for i, index in enumerate(indices):
            char[index] = new_v[i]
        return "".join(char)
        