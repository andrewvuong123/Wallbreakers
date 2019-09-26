class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # General Idea: Convert num to binary and then flip the bits and get the integer back
        binary = bin(num)
        b_list = list(binary)
        for i in range(2, len(b_list)):
            bit = b_list[i]
            if bit == "1":
                b_list[i] = '0'
            else:
                b_list[i] = '1'
        result = "".join(b_list)
        return int(result, 2) # base 2
        