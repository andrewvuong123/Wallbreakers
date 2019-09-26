class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # General Idea: Take all the vowels in the string into a list and reverse it, then iterate through each character in the string and if its a vowel then replace it with the item in the list.
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        insert = []
        for letter in s:
            if letter in vowels:
                insert.append(letter)
        insert.reverse()
        result = list(s)
        count = 0
        for i, letter in enumerate(result):
            if letter in vowels:
                result[i] = insert[count]
                count += 1
        return "".join(result)
        