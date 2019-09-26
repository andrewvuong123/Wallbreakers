class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # General Idea: Take the xor of x and y and count the number of bits that equal to one.
        xor = bin(x^y)
        count = 0
        for bit in xor:
            if bit == "1":
                count += 1
        return count
            