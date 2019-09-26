class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # General Idea: Join the list into one integer and add one then break it into a list again
        for i in range(0, len(digits)):
            digits[i] = str(digits[i])
        num = "".join(digits)
        num = int(num) + 1
        num = str(num)
        return list(num)