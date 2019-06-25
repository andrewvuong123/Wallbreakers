 class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)
        binary = binary[2:]
        n_list = list(str(binary))
        length = len(n_list)
        complement = 0
        for i in range(length):
            if n_list[i] == "0":
                n_list[i] = 1
            else:
                n_list[i] = 0
        n_list.reverse()
        for i in range(length):
            complement = complement + (2**i * n_list[i])
        return complement