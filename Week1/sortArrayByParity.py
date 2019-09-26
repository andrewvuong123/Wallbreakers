class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # General Idea: Create two separate lists of even/odd ints and then concatenate together
        even = []
        odd = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return (even + odd)        
        