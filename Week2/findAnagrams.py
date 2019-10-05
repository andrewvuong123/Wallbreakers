from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # General Idea: Have two counts, one for the pattern to check against and one for each window of s. If it matches append the index to a resulting list.

        p_c = Counter(p)
        s_c = Counter(s[0:len(p)])
        stop = len(s) - len(p) - 1
        result = []
        for i, letter in enumerate(s):
            if p_c == s_c:
                result.append(i)
            if i > stop:
                break
            if s_c[letter] > 1:
                s_c.update({letter:-1})
            else:
                del s_c[letter]
            s_c.update({s[i+len(p)]:1})
        return result
    