class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # General Idea: Initialize a counter variable and split the number in the range to see if the number mod by each digit is 0.
        
        count = 0
        divisible = []
        for num in range(left, right+1):
            count = 0
            denom = str(num);
            for digit in denom:
                if int(digit) != 0 and num % int(digit) == 0: 
                    count += 1
            if count == len(denom):
                divisible.append(num)
        return divisible
                    