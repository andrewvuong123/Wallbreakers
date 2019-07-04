class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # Idea: Create two lists consisting of odd and even indices values by list slicing [start:stop:step] and sort the created lists. Concatenate the odd and even list values and add to the set. Since set only contains unique values can return the length of set to find how many groups of special-equivalent strings exist.
        
        groups = set()
        for word in A:    
            even = "".join(sorted(word[0::2]))
            odd = "".join(sorted(word[1::2]))
            groups.add(odd+even)
        return len(groups)