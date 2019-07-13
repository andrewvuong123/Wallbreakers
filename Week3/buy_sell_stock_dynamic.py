class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Idea: Use Kadane's Algorithm to break the daily gains into subarrays of values minus the value previously. Then iterate through the subarray values. Update current subarray sum by taking the max between the previous subarray sum plus the index value and the index value itself. Then check if the current max is greater than the overall max, if it is then update the overall max.
        if len(prices) < 1:
            return 0
        
        profit = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        
        curr_max = 0
        overall_max = 0
        for i in range(len(profit)):
            curr_max = max(curr_max + profit[i], profit[i])
            if curr_max > overall_max:
                overall_max = curr_max
        return overall_max
            
            