class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # General Idea: Can have a pointer to child in g and cookie in s, if cookie satisfies child you can move pointer in both lists, else move pointer in s and check until cookie satisifes current child. Return the count once run out of cookies in s
        g.sort()
        s.sort()
        greed = 0
        cookie = 0
        count = 0
        while cookie < len(s) and greed < len(g):
            if s[cookie] >= g[greed]:
                cookie += 1
                greed += 1 
                count += 1
            else:
                cookie += 1
        return count
            