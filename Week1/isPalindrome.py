class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # General Idea: Convert into a list and remove all non alnum characters and then compare the original string with a reversed string.
        s_list = list(s)
        palindrome = []
        for i in s_list:
            if i.isalnum():
                palindrome.append(i.lower())
        original = "".join(palindrome)
        palindrome.reverse()
        reverse = "".join(palindrome)
        if original == reverse:
            return True
        else:
            return False
                