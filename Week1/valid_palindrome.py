class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        reg = list(s)
        non_alpnum = []
        for i, letter in enumerate(reg):
            if letter.isalpha() or letter.isdigit():
                continue
            else:
                non_alpnum.append(i)
        non_alpnum.reverse() # need to reverse to preserve list when popping
        for i in non_alpnum:
            reg.pop(i)
        rev = list(reg)
        rev.reverse()
        return reg == rev


class Solution_2(object):
    def isPalindrome_2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpnum = []
        s = s.lower()
        reg = list(s)
        for letter in reg:
            if letter.isalpha() or letter.isdigit():
                alpnum.append(letter)
            else:
                continue
        length = len(alpnum)
        i = 0
        j = 1
        while i < length/2:
            if alpnum[i] != alpnum[-j]:
                return False
            i += 1
            j += 1
        return True