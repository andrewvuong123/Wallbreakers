class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)
        binary = binary[2:]
        b_len = len(binary)
        dist = 0
        one = 0
        consecutive = [0]

        for i in range(b_len):
            if binary[i] == "1":
                one += 1
            if one == 1:
                dist += 1
            if one == 2:
                consecutive.append(dist)    
                one = 1
                dist = 1
        return max(consecutive)
        