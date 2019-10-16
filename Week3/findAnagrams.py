from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # General Idea: Iterate through slices of s and compare the sorted slice and p, if it matches then add the index to a result list and return result. Fails the last test case not optimal, solving by sorting not as optimal?
        
        p_list = list(p)
        p_list.sort()
        result = []
        for i in range(len(s)-len(p)+1):
            substring = list(s[i:i+len(p)])
            substring.sort()
            if substring == p_list:
                result.append(i)
        return result
            