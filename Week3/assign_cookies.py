class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Idea: Sort each list g and s. Check each value in the list, if the cookie satisfies the current child increment a count var by one and move the pointers in the list to the next values. If the cookie does not satisfy the child then increment the cookie pointer list.
        
        g.sort(), s.sort()
        count = 0 # var to keep count of satisfied children
        child, cookie = 0, 0 # pointer var for lists
        while child < len(g) and cookie < len(s): # while within the lists
            if s[cookie] >= g[child]:
                count += 1
                child += 1
                cookie += 1
            elif s[cookie] < g[child]:
                cookie += 1
        return count