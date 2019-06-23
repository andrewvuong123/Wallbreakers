class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        exp = len(digits) - 1
        total = 0
        for num in digits:
            total = total + num * 10**exp
            exp = exp - 1
        total = total + 1
        return list(str(total))