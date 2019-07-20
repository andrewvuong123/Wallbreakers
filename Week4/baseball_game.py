class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # Idea: Create a LIFO stack using list functions append and pop. If an integer, append to stack and add to sum, if its a C then subtract the last element from the sum and pop it from the stack, if it is a D then get the last element doubled and add that to the sum and stack, and if it is a + then get the sum of the last two elements and add that to the stack and sum.
        if not ops:
            return 0
        stack = []
        result = 0
        for char in ops:
            if char == "+":
                v_sum = stack[-1] + stack[-2]
                stack.append(v_sum)
                result += v_sum
            elif char == "D":
                double = stack[-1] * 2
                stack.append(double)
                result += double
            elif char == "C":
                result -= stack[-1]
                stack.pop()
            else:
                stack.append(int(char))
                result += int(char)
        return result