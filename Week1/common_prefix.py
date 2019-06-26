class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lcp = strs[0]
        for word in strs[1:]:
            j = 0
            curr = word
            while j < len(lcp) and j < len(curr) and curr[j] == lcp[j]:
                j += 1
            if j == 0:
                return ""
            lcp = lcp[0:j]
        return lcp
            