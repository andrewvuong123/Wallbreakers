class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_list, y_list = bin(x), bin(y)
        x_list, y_list = x_list[2:], y_list[2:]
        x_length = len(x_list)
        y_length = len(y_list)
        h_dist = 0
        while x_length != y_length:
            if x_length > y_length:
                y_list = "0" + y_list 
                y_length += 1
            if y_length > x_length:
                x_list = "0" + x_list 
                x_length += 1
        for i in range(x_length):
            if x_list[i] != y_list[i]:
                h_dist += 1
            
        return h_dist

class Solution_2(object):
    def hammingDistance_2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y 
        bin_num = bin(xor)
        bin_len = len(bin_num)
        h_dist = 0
        for i in range(bin_len):
            if bin_num[i] == "1":
                h_dist += 1
        return h_dist