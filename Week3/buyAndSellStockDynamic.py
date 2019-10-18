class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # General Idea: Can follow the dynamic Kadane's algorithm to get the max subarray sum fromo the differences of the profit values.
         
        
        def max_sum_subarray(arr):
            max_so_far = arr[0] # updates global sum overall 
            sum_elem_so_far = arr[0] # keeps track of contiguous sums, resets if current element is greater than sum
            for i in arr[1:]:
                sum_elem_so_far += i
                if i > sum_elem_so_far:
                    sum_elem_so_far = i
                if max_so_far < sum_elem_so_far:
                    max_so_far = sum_elem_so_far
            return max_so_far
        
        if len(prices) == 0:
            return 0
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i]-prices[i-1])
        return max_sum_subarray(diff)
    

        