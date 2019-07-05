from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Have two counts, one for the pattern to check against and one for each window of s. If it matches append the index to a resulting list.

        p_c = Counter(p)
        s_c = Counter(s[0:len(p)])
        stop = len(s) - len(p) - 1 # var to break out of loop
        result = []
        for i, letter in enumerate(s):
            if p_c == s_c: # if counters match then append the index to result list
                result.append(i)
            if i > stop:
                break
            if s_c[letter] > 1: # if letter repeats in string during pattern check, subtract one from count
                s_c.update({letter:-1})
            else:
                del s_c[letter] # delete item in counter and add the next to move window
            s_c.update({s[i+len(p)]:1})
        return result
    