class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # General Idea: Can follow the divide and conquer strategy similar to the maximum subarray sum problem. Run max subarray problem on the difference of the current and previous day.
         
        def max_mid_subarray(ar, low, mid, high):
            # left side
            curr_sum = 0
            left_sum = -100000
            for i in range(mid, low-1, -1):
                curr_sum = curr_sum + ar[i]
                if curr_sum > left_sum:
                    left_sum = curr_sum
            
            # right side
            curr_sum = 0
            right_sum = -100000
            for i in range(mid+1, high+1):
                curr_sum = curr_sum + ar[i]
                if curr_sum > right_sum:
                    right_sum = curr_sum
                
            
            return left_sum + right_sum
        
        def max_sum_subarray(ar, low, high):
            if low == high:
                return ar[low]
            
            mid = (low + high) // 2
            
            max_left = max_sum_subarray(ar, low, mid)
            max_right = max_sum_subarray(ar, mid+1, high)
            max_mid = max_mid_subarray(ar, low, mid, high)
            
            return max(max_left, max_right, max_mid)
        
        if len(prices) == 0:
            return 0
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i]-prices[i-1])
        return max_sum_subarray(diff, 0, len(prices) - 1)
        