class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Create a counter from s and use the most_common function to get a sequence from most counts to least. Iterate through the sequence and append the letter to a result list while the count is >= 1 and subtract the count. At the end return the joined result of the list.
        c = collections.Counter(s)
        result = []
        for letter, count in c.most_common():
            while count >= 1:
                result += [letter]
                count -= 1
                
        return "".join(result)
                