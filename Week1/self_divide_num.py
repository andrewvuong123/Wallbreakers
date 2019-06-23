class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        divisible = []
        count = 0
        for num in range(left, right+1):
            denom = list(str(num))
            count = 0
            for digit in denom:
                if int(digit) == 0:
                    break;
                if num % int(digit) == 0:
                    count += 1
                if count == len(denom):
                    divisible.append(num)
        return divisible